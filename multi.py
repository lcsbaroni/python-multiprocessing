#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
# import logging as log
import MySQLdb as mdb
# import shutil
import time
from datetime import datetime
from multiprocessing import Process, Queue
from math import ceil

from config import *

__doc__ = "Multiprocessing"

# Status
# load = 1;
# loading = 2;
# error = 3;
# success = 4;


def processqueue(queue):
    rows = queue.get()

    for row in rows:
        row_id = row[0]
        

        cursor_db.execute("UPDATE `temp_multiproccess` SET `id_status` = 2 WHERE `id` = %i;" % (row_id))
        db.commit()
        try:
            cursor_db.execute("UPDATE temp_multiproccess SET id_status = 4 WHERE id = %i;" % (row_id))
            db.commit()
        except Exception, e:
            cursor_db.execute("UPDATE temp_multiproccess SET id_status = 3 WHERE id = %i;" % (row_id))
            db.commit()
            print('Failed to process id: '+ str(e))


print(datetime.now().isoformat())

done = False
last_id = 0
processed = 0

while not done:
    db = mdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASS, MYSQL_DB)
    cursor_db = db.cursor()

    cursor_db.execute("SELECT * FROM  `temp_multiproccess` WHERE id_status = 1 \
        LIMIT %i;" % (PRODUCTS_PER_BATCH))
    
    rows = cursor_db.fetchall()

    if len(rows) == 0:
        print("done")
        done = True
        break
    
    total_rows = len(rows)
    processed += total_rows

    localProcess = TOTAL_PROCESS
    batch = int(ceil(float(total_rows) / localProcess))
    queue = Queue()

    if batch <= localProcess :
        localProcess = 1

    for i in xrange(0, total_rows, batch):
        queue.put(rows[i:i+batch])

    processes = [Process(target=processqueue, args=(queue,)) for i in range(localProcess)]

    for p in processes:
        print "inicio da thread"
        p.start()
        time.sleep(0.5)

    tLocalProcess = localProcess
    print "total process: " + str(tLocalProcess)
    while tLocalProcess > 0:
        for p in processes:
            if not p.is_alive():
                print "Fim da thread"
                tLocalProcess -= 1
        # time.sleep(3)

    for p in processes:
        print "mata thread"
        p.terminate()

    print "vou rodar de novo"

    db.close()

print(datetime.now().isoformat())