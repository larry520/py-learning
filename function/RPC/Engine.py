#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:dmsoft
@file: Engine.py
@time: 2020/03/22
"""

from .loggers import zmqPUB
from .tinyrpc.dispatch import RPCDispatcher
from .tinyrpc.server import RPCServer
from .tinyrpc.protocols.jsonrpc import *
from .tinyrpc.proxy.dotProxy import *
from .loggers.zmqPUB import *
from .loggers.zmqSUB import *
from .MESJoints.TcpSocket.socketClient import *
from .MESJoints.xmlConfigHandle import *



# ZMQ端口
# """系统各模块ZMQ初始化的端口"""
Logic_REP_port_I = {"value": 7150, "account": "Logic层的REP端bind的端口，GUI层的REQ端应该connect此端口"}  #
Vision_REP_port_I = {"value": 7250, "account": "Vision层的REP端bind的端口，Logic层的REQ端应该connect此端口"}  #
Logic_PUB_port_I = {"value": 7350, "account": "Logic层的PUB端bind的端口，GUI层的SUB端应该connect此端口"}  #
GUI_PUB_port_I = {"value": 7450, "account": "GUI层的PUB端bind的端口，Logic层的SUB端应该connect此端口"}  #
GUI_REP_port_I = {"value": 7550, "account": "GUI层的REP端bind的端口，Logic层的REQ端应该connect此端口"}  #




class Engine(RPCDispatcher):
    def __init__(self):
        super(Engine,self).__init__()
        self.dispatcher = RPCDispatcher()


    def initLogicFunc(self,reporters, url='tcp://localhost', retries=1, timeout=1, ctx=None):
        self.reporters = reporters
        self.createGProxy(reporters,url,retries,timeout,ctx)

        self.tcpClient = TcpClient(host=DotConfig.sysConfig.MESTcpServerIp_S["value"],port=DotConfig.sysConfig.MESTcpServerPort_I["value"])

    def createGProxy(self, reporters, url='tcp://localhost', retries=1, timeout=1, ctx=None):
        # 生成GUI的REQ代理
        self.GUI_Obj = dotGUIFunc(DotConfig.sysConfig.GUI_REP_port_I["value"], reporters, 0, url=url,
                                  retries=retries, timeout=timeout, ctx=ctx)

    def createVProxy(self, reporters, url='tcp://localhost', retries=1, timeout=1, ctx=None):
        # 生成vision的REQ代理
        self.visionObj = dotVisionFunc(DotConfig.sysConfig.Vision_REP_port_I["value"], reporters, 0, url=url,
                                       retries=retries, timeout=timeout, ctx=ctx)
        self.barCode_CV = ""

    def createMProxy(self, reporters):
        # 生成motion的REQ代理
        self.motionObj = dotMotionFunc(reporters)
        self.cameraLEDIndex = 0
        self.setSpeed(20)
        self.heatSwitch(0)
        self.setConveyorBlock(1, 1, 0)
        self.setConveyorBlock(1, 2, 0)
