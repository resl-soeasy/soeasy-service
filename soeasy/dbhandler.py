import mysql.connector

class DBHandler:
    def __init__(self):
        mydb = mysql.connector.connect(
            host    =   "localhost",
            user    =   "root",
            passwd  =   "dmdkdkr0"
        )