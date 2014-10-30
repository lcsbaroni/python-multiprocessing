#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import cpu_count

TOTAL_PROCESS = cpu_count()
PRODUCTS_PER_BATCH = 10000

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASS = ""
MYSQL_DB = "db"