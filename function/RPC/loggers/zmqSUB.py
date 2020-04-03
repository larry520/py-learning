from loggers.reporter import *
from loggers import levels

class zmqSubscriber(Thread):
    def __init__(self, port,head_type="",level=levels.REPORTER,url=None,ctx = None):
        super(zmqSubscriber, self).__init__()
        if not ctx:
            ctx = zmq.Context.instance()
        self.zmqSUB = ctx.socket(zmq.SUB)
        if url is None:
            url = 'tcp://localhost:' + str(port)
        self.zmqSUB.connect(url)
        self.url = url
        self.zmqSUB.setsockopt_string(zmq.SUBSCRIBE, head_type)
        time.sleep(0.5)
        self.head_type = head_type
        self._subFlag = False
        self.level = level
        self.subInfo = []
        self.subReport = Report()
        self.callerFlag = False

    def run(self):
        self._subFlag = True
        protocol = ReporterProtocol()
        if self.level == levels.DEBUG:
            print('ready to subscribe to %s,star with "%s"' % (str(self.url),self.head_type))
        while self._subFlag:
            try:
                head,ts,level,origin,data = self.zmqSUB.recv_multipart(zmq.NOBLOCK)
                self.subInfo=[str(head,"utf-8"),str(ts,"utf-8"),int(level),str(origin,"utf-8"),str(data,"utf-8")]
                self.subReport = protocol.parse_report(str(data, "utf-8"))
                if self.callerFlag ==True:
                    self.caller(self.subReport.data)
                if self.level == levels.DEBUG and int(level) == levels.REPORTER:
                    print(self.subInfo,self.subReport)
            except zmq.ZMQError :
                pass
            time.sleep(0.02)
        self.zmqSUB.setsockopt(zmq.LINGER, 0)
        self.zmqSUB.close()

    def registerCallback(self,func):
        self.callerFlag = True
        self.callbackFunc1 = func

    def caller(self,input):
        self.callbackFunc1(input)

    def kill(self):
        self._subFlag = False

    def __del__(self):
        self.kill()

if __name__ == "__main__":
    def callback(par):
        print(par)
    report_listener = zmqSubscriber(7451,level=levels.DEBUG)
    report_listener.start()
    report_listener1 = zmqSubscriber(7350,head_type="10005",level=levels.DEBUG)
    report_listener1.start()
    report_listener1.registerCallback(callback)
