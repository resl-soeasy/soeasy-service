import mysql.connector
import logging
import sys

class DBHandler:
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                host    =   "localhost",
                user    =   "soeasy",
                password  =   "soeasy",
                database=   "soeasy"
            )
        except Exception as e:
            logging.error("db connect failed (message : {})".format(e))
            sys.exit(1)

        self.cursor = self.mydb.cursor()