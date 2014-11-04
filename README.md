python-multiprocessing
======================

python-multiprocessing

This script is an example of multiprocess works with python.

To execute it, is necessary create a table "temp_multiproccess"

CREATE TABLE `temp_multiproccess` (
  `id` INT(10) NOT NULL AUTO_INCREMENT,
    `id_status`  INT(10) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=INNODB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

INSERT INTO temp_multiproccess (id, id_status)  
    VALUES 
            ( NULL, 1 ),
                    ( NULL, 1 ),
                            ( NULL, 1 ),
                                    ( NULL, 1 ),
                                            ( NULL, 1 ),
                                                    ( NULL, 1 ),
                                                            ( NULL, 1 ),
                                                                    ( NULL, 1 ),
                                                                            ( NULL, 1 ),
                                                                                    ( NULL, 1 ),
                                                                                            ( NULL, 1 ),
                                                                                                    ( NULL, 1 ),
                                                                                                            ( NULL, 1 ),
                                                                                                                    ( NULL, 1 ),
                                                                                                                            ( NULL, 1 ),
                                                                                                                                    ( NULL, 1 ),
                                                                                                                                            ( NULL, 1 ),
                                                                                                                                                    ( NULL, 1 ),
                                                                                                                                                            ( NULL, 1 ),
                                                                                                                                                                    ( NULL, 1 ),
                                                                                                                                                                            ( NULL, 1 );



So, execute:
python2.7 multi.py
