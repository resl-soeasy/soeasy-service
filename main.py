#!/usr/bin/python3.5
# -*- coding:UTF-8 -*-
import threading
import logging
import inspect
from threading import Thread
import datetime
import time
import sys
from soeasy import configure, logger, GpioDigitalCommand
import sys
import socketserver
import json

JSON = {}

class SoeasyRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        global JSON
        # self.data = self.request.recv(1024)
        receive_data = self.request
        receive_data = json.loads(receive_data[0].decode("utf-8"))
        logging.info("Request Handler Receive Data : {}".format(receive_data["index"]))
        # self.request.sendall("result")
        index = receive_data["index"]

        logging.info(JSON)

        gpio_digital_command = GpioDigitalCommand.GpioDigitalCommand()
        gpio_digital_command.set_configure(index=JSON[int(index)])

        logging.info(gpio_digital_command.get_value())

        result = str(gpio_digital_command.get_value()["out"]).replace("b'", "").replace("\\n'", "")
        logging.info(result)

        if result == "0":
            gpio_digital_command.set_value(1)
        else:
            gpio_digital_command.set_value(0)

        


class Init:
    def set_request_server(self):
        try:
            server = socketserver.UDPServer(("localhost", 9980), SoeasyRequestHandler)
            server.serve_forever()
            logging.info("Request Receive Server Start")
        except Exception as e:
            logging.error("Start Request Server Failed ({})".format(e))

    def configure(self):
        global JSON
        self.configure = configure.Configure()
        JSON = self.configure.get_gpio_list()

@logger.AddLogger(log_location="/var/log/soeasy.log", log_mode=logging.INFO)
def main():
    Init().configure()

    gpio_digital_command = GpioDigitalCommand.GpioDigitalCommand()
    gpio_digital_command.set_configure(index=JSON[10])

    #logging.info(gpio_digital_command.get_value())
    Init().set_request_server()


if __name__ == '__main__':
    main()