import logging
from soeasy import dbhandler

class Configure(dbhandler.DBHandler):
    def __init__(self):
        logging.info("Get Configuration")

    def get_gpio_list(self):
        logging.info("Get GPIO List")
