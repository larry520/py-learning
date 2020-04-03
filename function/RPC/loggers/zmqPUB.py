import json
import time
import datetime
from threading import Thread
import threading
import zmq
import logging
from ..loggers.reporter import *
from ..loggers import levels
# from Tools import zmqports
from ..tinyrpc.exc import RPCError





class optPublisher(object):
    def __init__(self, identity):
        self.identity = identity

    def publish(self,msg,id_postfix=None,level=levels.DEBUG):
        self.opt_publish(PUB_COMMON,msg,id_postfix,level)

    def opt_publish(self,head_type,msg,id_postfix=None,level=levels.DEBUG):
        t = datetime.datetime.now()
        ts = datetime.datetime.strftime(t, '%Y-%m-%d %H:%M:%S.%f')
        id_str = self.identity
        if id_postfix:
            id_str = id_str + '_' + id_postfix
        if hasattr(self, '_send'):
            self._send(head_type,ts,level,id_str,msg)

class zmqPublisher(optPublisher):
    def __init__(self,identity,port,ctx = None):
        super(zmqPublisher, self).__init__(identity)
        if not ctx:
            ctx = zmq.Context.instance()
        self.zmqPUB = ctx.socket(zmq.PUB)
        self.zmqPUB.setsockopt_string(zmq.IDENTITY, identity)
        url = 'tcp://*:' + str(port)
        self.zmqPUB.bind(url)
        print("Publisher[%s] URL is:%s"%(identity,url))
        logging.info("Publisher[%s] URL is:%s"%(identity,url))
        time.sleep(0.5)  # 加延时0.5s用来确保当客户端先运行时，服务端与客户端连接成功后才pub数据。
        self.lock = threading.Lock()

    def _send(self,head_type,ts,level,id_str,msg):
        # zmq socket is not thread safe
        self.lock.acquire()
        self.zmqPUB.send_multipart([str(head_type).encode("utf-8"),
                                    str(ts).encode("utf-8"),
                                    str(level).encode("utf-8"),
                                    str(id_str).encode("utf-8"),
                                    str(msg).encode("utf-8")])
        if level == levels.DEBUG:
            print("pub:"+str([head_type,ts,levels.get_name(level),id_str,msg]))
        self.lock.release()

    def close(self):
         if not self.zmqPUB.closed:
            if zmq is None:  # the zmq module may have been released by this time
                return
            self.zmqPUB.setsockopt(zmq.LINGER, 0)
            self.zmqPUB.close()

    def __del__(self):
        self.close()



if __name__ == "__main__":
    publisher = zmqPublisher("dotVision",5551)
    reporter1 = optReporter("10011",publisher)
    reporter2 = optReporter("10011",publisher)
    #time.sleep(1)
    log = 0
    for i in range(10):
        if  log>10:
            log = 0
        reporter1.opt_report(events.VISION_ERROR,error={"errorCode":log,"msg":""},level=levels.DEBUG)
        reporter2.opt_report( events.VISION_ERROR,error={"errorCode":log+1000,"msg":""},level=levels.DEBUG)
        time.sleep(2)
        log += 1

    publisher.close()
