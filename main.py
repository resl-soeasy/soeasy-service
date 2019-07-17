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

class SoeasyRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        logging.info("Request Handler Receive Data : {}".format(self.data))
        self.request.sendall(self.data.upper())

class Init:
    def set_request_server(self):
        HOST, PORT = "localhost", 9980

        try:
            with socketserver.TCPServer((HOST, PORT), SoeasyRequestHandler) as server:
                server.serve_forever()
                logging.info("Request Receive Server Start")
        except Exception as e:
            logging.error("Start Request Server Failed ({})".format(e))

    def configure(self):
        self.configure = configure.Configure()
        self.configure.get_gpio_list()

@logger.AddLogger(log_location="/var/log/soeasy.log", log_mode=logging.INFO)
def main():
    Init().configure()
    Init().set_request_server()

if __name__ == '__main__':
    main()