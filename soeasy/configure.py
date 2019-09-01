import logging
from soeasy import dbhandler

class Configure(dbhandler.DBHandler):
    hardware = ""

    def __init__(self):
        dbhandler.DBHandler.__init__(self)
        logging.info("Get Configuration")

    def get_gpio_list(self):

        dict_test = {}
        self.cursor.execute("SELECT * FROM GPIO_LIST", "")
        result = self.cursor.fetchall()

        for record in result:
            logging.info(record)
            dict_test[record[0]] = record[1]

        logging.info("Get GPIO List")

        return dict_test
