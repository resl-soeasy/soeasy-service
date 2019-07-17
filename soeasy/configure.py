import logging
from soeasy import dbhandler

class Configure(dbhandler.DBHandler):
    hardware = ""

    def __init__(self):
        dbhandler.DBHandler.__init__(self)
        logging.info("Get Configuration")

    def get_gpio_list(self):
        self.cursor.execute("SELECT * FROM GPIO_LIST", "")
        result = self.cursor.fetchall()

        for record in result:
            logging.info(record)

        logging.info("Get GPIO List")

        return result
