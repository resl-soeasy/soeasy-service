import logging
from soeasy import dbhandler
from abc import *

GPIO_SYSFS = "/sys/class/gpio/gpio"

class Command(dbhandler.DBHandler):
   
    @abstractmethod
    def set_index(self, index=0):
        logging.info("set gpio index ({})".format(index))

    @abstractmethod
    def set_export(self, direction="in"):
        logging.info("set_export")

    @abstractmethod
    def set_direction(self, direction="in"):
        logging.info("Bring the record information from the table. (TableName : {}, Language : {})", self.table_name, self.language)

    @abstractmethod
    def set_value(self, value=0):
        pass

    @abstractmethod
    def save(self):
        pass