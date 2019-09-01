import logging
import threading

class Thread(threading.Thread):
    def __init__(self, configure, queue):
        threading.Thread.__init__(self)
        self.configure = configure
        self.queue = queue
        logging.info("Consumer Thread Start")

    def run(self):
        while True:
            message = self.queue.get()
            logging.info("Real Event Worker Command Message {}".format(message))
            real_event_worker_command.set_eventlog(message)
            real_event_worker_command.send_data()
