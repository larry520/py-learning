#  -*- coding:utf-8  -*-
import socket
import threading
import time
import sys
import traceback

from function.RPC.MESJoints import MESProtocol as _protocol

class TcpClient(object):
    def __init__(self, host = '127.0.0.1', port = 8880,BUFFSIZE = 1024):
        self.host = host
        self.port = port
        self.buffsize = BUFFSIZE
        self.addr = (self.host, self.port)


        # self.start_flag = _protocol.DATAHEAD
        # self.stop_flag = _protocol.DATAHEAD
        # self.separator = _protocol.SEPARATOR

        # print('socket initially finally!')
        self.partNum = ""
        self.breakList = []
        self.DotList = []
        self.WholeBreak = None
        self.bConnected = False
        self.bDoConn = False

    def conn(self):
        try:
            if not self.bConnected:
                self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.clientsocket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
                self.clientsocket.setblocking(True)
                self.clientsocket.settimeout(30)

                self.clientsocket.connect(self.addr)
                self.bConnected = True
        except Exception as e:
            self.bConnected = False
        self.bDoConn = True
        return self.bConnected

    def _reconnect(self):
        try:
            self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.clientsocket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            self.clientsocket.setblocking(True)
            self.clientsocket.settimeout(30)
            self.clientsocket.connect(self.addr)
            self.bConnected = True
        except Exception as e:
            self.bConnected = False
            print(e)

    def recvMsg(self, bufsize):
        try:
            if self.bConnected:
                rdata = self.clientsocket.recv(bufsize).decode('utf8')
                # print("rec from service: ", rdata, '\n')
                if rdata:
                    self.parseMsg(rdata)
                else:
                    print("server closed")
                    self.bConnected = False
                    return False
        except Exception as e:
            print(e.__str__())
            raise Exception(e.__str__())
        return True

    def parseMsg(self,rcvdata):
        # rcvdata = "#1021;12345;[SN001,1,0];[SN002,2,0];[SN002,3,0];[SN002,4,2];[SN002,5,0];[SN002,6,2];OK;#"
        # a = [m.start() for m in re.finditer("#", rcvdata)]
        # print(a)

        # self.partNum = ""
        # self.breakList = []
        boardStateList = []
        # print("recvdata:",rcvdata)
        splitData = rcvdata[1:-2].split(_protocol.TcpProtocol.SEPARATOR)
        # print("split:",splitData)
        if splitData[0] == _protocol.TcpProtocol.RspProtocol.partnumRspSerial:
            self.partNum = splitData[2]
        elif splitData[0] == _protocol.TcpProtocol.RspProtocol.statusRspSerial:
            if splitData[len(splitData) - 1] == "OK":
                self.WholeBreak = False
                for nn in range(2, len(splitData) - 1):
                    boardStateList = splitData[nn].replace("[", "").replace("]", "").split(",")
                    # print("boardStateList:{0}".format(boardStateList))
                    if boardStateList[2] == "2":
                        self.breakList.append(boardStateList[1])
                        # print("     breakBoard:{0}".format(boardStateList[1]))
                        # print("         breakList:{0}".format(self.breakList))
                    elif boardStateList[2] == "0":
                        self.DotList.append(boardStateList[1])
                        # print("         DotList:{0}".format(self.DotList))
            elif splitData[len(splitData) - 1] == "NG":
                self.WholeBreak = True
        # return WholeBreak,breakList

    def SerializeMsg(self,
                     serial,
                     barCode,
                     reMsg = "",
                     start_flag = _protocol.TcpProtocol.DATAHEAD,
                     stop_flag = _protocol.TcpProtocol.DATAHEAD,
                     separator = _protocol.TcpProtocol.SEPARATOR
                     ):
        # start_flag += separator   # #后不用加;
        # stop_flag += separator
        serial += separator
        barCode += separator
        if reMsg !="" and reMsg !=None:
            reMsg+=separator
        return str(start_flag+serial+barCode+reMsg+stop_flag)

    def sendMsg(self,data):
        try:
            self.clientsocket.send(data.encode('utf8'))
        except Exception as e:
            raise Exception(e.__str__())
        return True

    def closeClient(self):
        try:
            if self.bConnected:
                self.clientsocket.close()
                self.bConnected = False
        except Exception as e:
            print(e.__str__())
            return False
        return True

    def run(self):
        connect_thread = threading.Thread(target=self.conn)
        connect_thread.daemon = True
        connect_thread.start()

    def ReqPartNum(self,barCode=""):
        try:
            self.partNum = ""
            serial = _protocol.TcpProtocol.ReqProtocol.partnumReqSerial
            # barCode = ""
            data = self.SerializeMsg(serial,barCode)
            bSend = self.sendMsg(data)
            if not bSend:
                return 26002,"Send Msg Failed!"
            bRecv = self.recvMsg(self.buffsize)
            if not self.bConnected:
                return 26005,"server close!"
            if not bRecv:
                return 26003,"Recv Msg Failed"
            if self.partNum == None or self.partNum =="":
                return 26003, "Wrong Recv Msg!"
        except  Exception as e:
                return 26004, "Request PartNum failed!:{0}".format(e.__str__())
        return 0,"Request PartNum :{0}".format(self.partNum.__str__())

    def ReqBreakList(self, barCode):
        try:
            self.breakList = []
            self.DotList = []
            self.WholeBreak = None
            serial = _protocol.TcpProtocol.ReqProtocol.statusReqSerial
            barCode = barCode
            data = self.SerializeMsg(serial, barCode)
            bSend = self.sendMsg(data)
            if not bSend:
                return 26002, "Send Msg failed"
            bRecv = self.recvMsg(self.buffsize)     #短连接
            if not self.bConnected:
                return 26005,"server close!"
            if not bRecv:
                return 26003, "Recv Msg Failed"
            if self.WholeBreak == None:
                return 26003, "Wrong Recv Msg!"
        except  Exception as e:
            return 26004, "Request board status failed!:{0}".format(e.__str__())
        return 0,"Request board status successed!"

    def doLoopReqPartTest(self):
        while True:
            time.sleep(0.5)
            self.ReqPartNum()

def test():
    # t = TcpClient(port=8282)
    t = TcpClient(port=8880)
    t.run()
    while not t.bDoConn:
        time.sleep(0.1)
        pass
    if t.bConnected:
        t.ReqBreakList("132646030030")
        # t.ReqPartNum()
        while t.partNum == "":
            if not t.bConnected:
                t.closeClient()
                break
            pass
        time.sleep(1)
        print("connect state:",t.bConnected)
    print("print ", t.partNum, t.WholeBreak, t.breakList)


def test2():
    t1 = TcpClient()
    t1.run()
    while not t1.bDoConn:
        time.sleep(0.1)
        pass
    if t1.bConnected:
        loopReq_thread = threading.Thread(target=t1.doLoopReqPartTest)
        loopReq_thread.setDaemon(True)
        loopReq_thread.start()

    for tempI in range(1000):
        for tempII in range(1000000):
            print("----")
            if t1.partNum != "":
                print("ddddd",t1.partNum)
            time.sleep(0.5)

def test3():
    t1 = TcpClient(port=8282)
    a = t1.conn()
    print(str(a))
    time.sleep(2)
    b = t1.conn()
    print(str(b))


if __name__ == "__main__" :
    # import time
    # boardBarCode = "111"
    # mesfilename = "DOT_%s_%04d%02d%02d%02d%02d%02d" % (str(boardBarCode), int(time.localtime().tm_year), int(time.localtime().tm_mon),int(time.localtime().tm_mday),int(time.localtime().tm_hour), int(time.localtime().tm_min), int(time.localtime().tm_sec))  # TODO 文件名需要确认
    # print(mesfilename)
    test3()