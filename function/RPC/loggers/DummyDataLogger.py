#!/usr/bin/env python
# encoding=utf-8


import zmq
import os
import re

class DataLogger(object):
    def __init__(self, logFile):
        if os.path.exists(os.path.dirname(logFile)):
            os.mkdir(os.path.dirname(logFile))

        self.fp = open(logFile, 'w+')
        self.subscriber = zmq.Context().socket(zmq.SUB)
        self.subscriber.connect('tcp://localhost:' + str(6250))
        self.subscriber.setsockopt(zmq.SUBSCRIBE, "101")

        self.loopData = []

    def subMesg(self):
        itemStart = None
        itemEnd = None

        itemStartPattern = '"event": 2'
        itemEndPattern = '"event": 3'

        while True:
            topic, ts, level, origin, data = self.subscriber.recv_multipart(zmq.NOBLOCK)

            if re.search(itemStartPattern, data) != None:
                itemStart = ts

            elif re.search(itemEndPattern, data) != None:
                if itemStart != None:
                    itemEnd = ts
                    self.loopData.append()



if __name__ == '__main__':
    pass