#! /usr/bin/env python
#-*- coding:utf-8 -*-

import socket
import threading
from time import ctime
from function.RPC.MESJoints import MESProtocol as  _protocol

class ThreadedServer(object):
    def __init__(self, host, port):
        self.start_time = ctime()
        print('starting ', self.start_time)

        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        print("listen on port : %d" % self.port)
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            # client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    response = data.decode('utf8')
                    print("recvLen: ",len(response),"data: ",response," yoo!")

                    rspSerialStr, barCode = self.parseMsg(response)
                    rspData = self.getRsp(rspSerialStr,barCode)
                    client.send(rspData)
                    print("sendLen: ",len(rspData),"data: ",rspData.decode("utf-8"))
                else :
                    # raise Exception('Error!')
                    pass
            except Exception as e:
                client.close()
                print(e.__str__())
                return False

    def parseMsg(self, response):
        rspSerialStr = ""
        barCode = ""
        # response = "#0010;;#"
        if str(response).endswith("#") and str(response).startswith("#"):
            splitData = response[1:-2].split(";")
            print(splitData)
            if splitData[0] == _protocol.TcpProtocol.ReqProtocol.partnumReqSerial:
                rspSerialStr = _protocol.TcpProtocol.RspProtocol.partnumRspSerial
            elif splitData[0] == _protocol.TcpProtocol.ReqProtocol.statusReqSerial:
                rspSerialStr = _protocol.TcpProtocol.RspProtocol.statusRspSerial

            barCode = str(splitData[1])
        return rspSerialStr,barCode

    def getRsp(self, rspSerialStr,barCode):
        rspData = ""
        if rspSerialStr != None and rspSerialStr != "":
            if rspSerialStr == _protocol.TcpProtocol.RspProtocol.partnumRspSerial:
                rspData = self.SerializeMsg(rspSerialStr,barCode,reMsg="2019-9-6AOITest")
            elif rspSerialStr == _protocol.TcpProtocol.RspProtocol.statusRspSerial:
                boardMsg= "[110806220001,1,2];[110806220001,2,0];[110806220001,3,0];[110806220001,4,2];[110806220001,5,0];[110806220001,6,2];[110806220001,7,0];[110806220001,8,0];[110806220001,9,0];[110806220001,10,0];[110806220001,11,0];[110806220001,12,0];[110806220001,13,0];[110806220001,14,0];[110806220001,15,0];[110806220001,16,0];[110806220001,17,0];[110806220001,18,0];[110806220001,19,0];[110806220001,20,0];[110806220001,21,0];[110806220001,22,0];[110806220001,23,0];[110806220001,24,0];[110806220001,25,0];[110806220001,26,0];[110806220001,27,0];[110806220001,28,0];[110806220001,29,0];[110806220001,30,0];OK"
                rspData = self.SerializeMsg(rspSerialStr, barCode, reMsg=boardMsg)
        return rspData.encode("utf-8")

    def SerializeMsg(self,
                     serial,
                     barCode,
                     reMsg = "",
                     start_flag = _protocol.TcpProtocol.DATAHEAD,
                     stop_flag = _protocol.TcpProtocol.DATAEND,
                     separator = _protocol.TcpProtocol.SEPARATOR
                     ):
        # start_flag += separator   # #后不用加;
        # stop_flag += separator
        serial += separator
        barCode += separator
        if reMsg !="" and reMsg !=None:
            reMsg+=separator
        return str(start_flag+serial+barCode+reMsg+stop_flag)


if __name__ == "__main__":
    port_num = 8282
    ThreadedServer('',port_num).listen()