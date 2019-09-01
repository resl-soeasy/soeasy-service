import mysql.connector
import logging

class DBHandler:
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                host    =   "localhost",
                user    =   "soeasy",
                password  =   "soeasy",
                passwd = "soeasy",
                database=   "soeasy"
            )
        except Exception as e:
            logging.error("db connect failed (message : {})".format(e))

        self.cursor = self.mydb.cursor()