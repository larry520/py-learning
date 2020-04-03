
import threading
import select
import errno

import tinyrpc
import zmq
import logging
import socket


class HB(threading.Thread):
    def __init__(self, seconds, publisher):
        super(HB, self).__init__()
        self.seconds = seconds
        self.publisher = publisher

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # ctx = zmq.Context()
        # self.socket = ctx.socket(zmq.REQ)
        # self.socket.connect("tcp://127.0.0.1:32768")

        # self.poller = zmq.Poller()
        # self.poller.register(self.socket, zmq.POLLIN)
        
    def run(self):
        while True:
            try:
                r, w, e = select.select([self.sock], [], [], self.seconds)
            except (OSError, select.error) as e:
                if e.args[0] != errno.EINTR:
                    raise

            self.publisher.publish(tinyrpc.FCT_HEARTBEAT)
            # logging.warn("heart beat")

        # while True:
        #     try:
        #         events = dict(self.poller.poll(self.seconds * 1000))
        #     except (OSError, zmq.Again) as e:
        #         if e.args[0] != errno.EINTR:
        #             raise
        #
        #     if len(events) == 0:
        #         logging.warn("heart beat")
        #         self.publisher.publish(tinyrpc.FCT_HEARTBEAT)



if __name__ == '__main__':
    FORMAT = "%(asctime)s %(levelname)s %(filename)s %(message)s"
    logging.basicConfig(format=FORMAT, level=logging.INFO)

    hb = HB(5, None)
    hb.start()