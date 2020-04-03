#  -*- coding:utf-8  -*-
import datetime
import time
import sys
import os
from Tools.xmlConfigHandle import *
import MESJoints.MESProtocol as _protocol
from goto import with_goto
"""=========================================MES file操作=================================="""


def createDOTMESResListFun(dotPathList,
                           DOTPCBList,
                           barCode,
                           startTime,
                           endTime,
                           Program,
                           pathSpeedList,
                           CurrentTrackT,
                           CurrentTrackLowerT,
                           CurrentTrackUpperT,
                           SetValveT,
                           CurrentValveT,
                           curValveLowerT,
                           curValveUpperT,
                           SingleDotWeight,
                           singleDotLowerWeight,
                           singleDotUpperWeight,
                           DotRadius,
                           isAllPcbBreak,
                           DotRes = 'OK',
                           Error = '',
                           ):
    """
    创建点胶的MES结果列表
    :param dotPathList: 点胶路径列表  with INIT
    :param DOTList:  执行的板子编号列表
    :param barCode:  产品码
    :param startTime: 开始时间
    :param endTime: 结束时间
    :param Program: 工程文件名
    :param pathSpeedList: 点胶速度列表
    :param WorkHeightList: 工作高度列表
    :param CurrentTrackT: 当前轨道温度
    :param CurrentTrackLowerT: 当前轨道温度下限值
    :param CurrentTrackUpperT: 当前轨道温度上限值
    :param SetValveT: 设置胶阀温度
    :param CurrentValveT: 当前胶阀温度
    :param curValveLowerT: 当前胶阀温度下限值
    :param curValveUpperT: 当前胶阀温度上限值
    :param SingleDotWeight: 单点胶重
    :param singleDotLowerWeight: 单点胶重下限值
    :param singleDotUpperWeight: 单点胶重上限值
    :param DotRadius: 单点胶半径
    :param isAllpcbBreak: 是否直接跳过整板
    :param DotRes: 结果
    :param Error:
    :return:
    """
    DOTMESResList = []
    if isAllPcbBreak:
        DotRes = "ng"
    FileHead = _protocol.FileProtoCol.FileSEPATOR.join([barCode,startTime,endTime,DotRes])
    DOTMESResList.append(FileHead)    #文件头部
    for dpli in range(len(DOTPCBList)):   #TODO 此处速度和高度需确定用List时是否需要带双引号，需要则添加双引号并将list中的单引号改成双引号(参考TestSpeedList)
        i = int(DOTPCBList[dpli])
        DotSpeedList = []
        WorkHeightList = []
        programLine = _protocol.FileProtoCol.FileSEPATOR.join([str(i),'Program','','',Program,'','T',str(DotRes),Error])
        DOTMESResList.append(programLine)

        for si in dotPathList:
            if si['sItem'] == 'PATH':
                if str(si['nPCBNum']) == str(i):
                    pathSpeedListCC = pathSpeedList[:]
                    for sped in pathSpeedListCC:
                        if sped[0] == si['nIndex']:
                            DotSpeedList.append(sped)
                            pathSpeedList.remove(sped)
                    # pathSpeed = [si['nIndex'],si['dSpeed']]
                    pathHeight = [si['nIndex'],si['dZWorkDis']]
                    # DotSpeedList.append(pathSpeed)
                    WorkHeightList.append(pathHeight)
        print(str(DotSpeedList)[1:-1])
        DotSpeedLine = _protocol.FileProtoCol.FileSEPATOR.join([str(i),'DotSpeed','','',str(DotSpeedList),'mm/s','T',str(DotRes),Error])
        DOTMESResList.append(DotSpeedLine)

        WorkHeightLine = _protocol.FileProtoCol.FileSEPATOR.join([str(i), 'WorkHeight', '', '', str(WorkHeightList), 'mm/s', 'T', str(DotRes),Error])
        DOTMESResList.append(WorkHeightLine)

        CurrentTrackTLine = _protocol.FileProtoCol.FileSEPATOR.join([str(i), 'CurrentTrackT', str(CurrentTrackLowerT), str(CurrentTrackUpperT), str(CurrentTrackT), 'C', 'N', str(DotRes),Error])
        DOTMESResList.append(CurrentTrackTLine)

        SetValveTLine = _protocol.FileProtoCol.FileSEPATOR.join([str(i), 'SetValveT', '', '', str(SetValveT), 'C', 'T', str(DotRes),Error])
        DOTMESResList.append(SetValveTLine)

        CurrentValveTLine = _protocol.FileProtoCol.FileSEPATOR.join([str(i), 'CurrentValveT',str(curValveLowerT), str(curValveUpperT), str(CurrentValveT), 'C', 'N', str(DotRes),Error])
        DOTMESResList.append(CurrentValveTLine)

        SingleDotWeightLine = _protocol.FileProtoCol.FileSEPATOR.join([str(i), 'SingleDotWeight', str(singleDotLowerWeight), str(singleDotUpperWeight), str(SingleDotWeight), 'mg', 'N', str(DotRes),Error])
        DOTMESResList.append(SingleDotWeightLine)

        DotRadiusLine = _protocol.FileProtoCol.FileSEPATOR.join([str(i), 'DotRadius', '', '', str(DotRadius), 'mm', 'T', str(DotRes),Error])
        DOTMESResList.append(DotRadiusLine)
        # DOTMESResList.append('')

    DOTMESResList.append(_protocol.FileProtoCol.FileEND)        #文件尾部
    return DOTMESResList


def createAOIMESResListFun_old(AOISeqList,
                        AOIPCBList,
                        barCode,
                        startTime,
                        endTime,
                        Program,
                        flySpeed,
                        flyLight,
                        upperLimitList,
                        lowerLimitList,
                        isAllPcbBreak,
                        AOIResult,
                        ngList,
                        Error = ''
                           ):
    """
    创建AOI的MES结果列表
    :param AOISeqList: AOI序列
    :param AOIPCBList: 执行的AOI板子编号列表
    :param barCode: 产品码
    :param startTime: 开始时间
    :param endTime: 结束时间
    :param Program: 工程文件名
    :param flySpeed: 飞拍速度
    :param flyLight: 飞拍光源
    :param upperLimit: AOI检测上限列表
    :param lowerLimit: AOI检测下限列表
    :param isAllpcbBreak: 是否直接跳过整板
    :param AOIResult: 整体(大板)AOI结果
    :param ngList: ng列表
    :param Error:
    :return:
    """
    AOIMESResList = []
    WholeAOIRes = 'ok'
    if isAllPcbBreak:
        WholeAOIRes = "ng"
    for ari in range(len(AOIResult)):
        if AOIResult[ari] == 'ng':
            WholeAOIRes = 'ng'
            break
    FileHead = _protocol.FileProtoCol.FileSEPATOR.join([barCode,startTime,endTime,WholeAOIRes])
    AOIMESResList.append(FileHead)    #文件头部
    for apli in  range(len(AOIPCBList)):
        i = int(apli)   # pcb编号序列与飞拍序列要一致
        pcbNum = AOIPCBList[i]
        pcbUpper = upperLimitList[i]
        pcbLower = lowerLimitList[i]

        programLine = _protocol.FileProtoCol.FileSEPATOR.join([str(i),'Program','','',Program,'','T',str(AOIResult[i]),Error])
        AOIMESResList.append(programLine)

        PCBResultLine = _protocol.FileProtoCol.FileSEPATOR.join([str(pcbNum), 'ALL', str(pcbLower), str(pcbUpper), '', '', 'N', str(AOIResult[i]), Error])
        AOIMESResList.append(PCBResultLine)

        pcbNgList = ngList[i]
        for nn in range(len(pcbNgList)):   #遍历添加ng边的结果
            GlueValue = 0
            borderLower = float(pcbNgList[nn][1])   #当前边下限
            borderUpper = float(pcbNgList[nn][2])   #当前边上限
            if borderLower>pcbUpper or borderLower<pcbLower:
                GlueValue = borderLower
            elif borderUpper > pcbUpper or borderUpper < pcbLower:
                GlueValue = borderUpper
            AOIBorderLine = _protocol.FileProtoCol.FileSEPATOR.join(
                [str(pcbNum), str(pcbNgList[nn][0]), '', '', str(GlueValue), '', 'T', 'ng', Error])
            AOIMESResList.append(AOIBorderLine)

        passFlySpeedLine=  _protocol.FileProtoCol.FileSEPATOR.join([str(pcbNum), 'flySpeed', '', '', str(flySpeed), 'mm/s', 'T', str(AOIResult[i]), Error])
        AOIMESResList.append(passFlySpeedLine)

        passFlyLightLine=  _protocol.FileProtoCol.FileSEPATOR.join([str(pcbNum), 'flyLight', '', '', str(flyLight), '', 'T', str(AOIResult[i]), Error])
        AOIMESResList.append(passFlyLightLine)
        AOIMESResList.append('')

    AOIMESResList.append(_protocol.FileProtoCol.FileEND)  # 文件尾部
    return AOIMESResList

def createAOIMESResListFun(AOISeqList,
                        AOIPCBList,
                        barCode,
                        startTime,
                        endTime,
                        Program,
                        flySpeed,
                        flyLight,
                        upperLimitList,
                        lowerLimitList,
                        isAllPcbBreak,
                        AOIResult,
                        ngList
                           ):
    """
    创建AOI的MES结果列表
    :param AOISeqList: AOI序列
    :param AOIPCBList: 执行的AOI板子编号列表
    :param barCode: 产品码
    :param startTime: 开始时间
    :param endTime: 结束时间
    :param Program: 工程文件名
    :param flySpeed: 飞拍速度
    :param flyLight: 飞拍光源
    :param upperLimit: AOI检测上限列表
    :param lowerLimit: AOI检测下限列表
    :param isAllpcbBreak: 是否直接跳过整板
    :param AOIResult: 整体(大板)AOI结果
    :param ngList: ng列表
    :return:
    """
    AOIMESResList = []
    WholeAOIRes = 'ok'
    if isAllPcbBreak:
        WholeAOIRes = "ng"
    for ari in range(len(AOIResult)):
        if AOIResult[ari] != 'ok':
            WholeAOIRes = 'ng'
            break
    FileHead = _protocol.FileProtoCol.FileSEPATOR.join([barCode,startTime,endTime,WholeAOIRes])
    AOIMESResList.append(FileHead)    #文件头部
    # AOISeqList.pop(0)
    for apli in  range(len(AOISeqList)):
        i = int(apli)
        pcbNum = AOISeqList[i]["nPCBNum"]
        pcbUpper = upperLimitList[i]
        pcbLower = lowerLimitList[i]

        piceResult = str(AOIResult[i])
        Error = ""
        if str(AOIResult[i]) != "ok":
            piceResult = "ng"
            Error = "CYG"+str(AOIResult[i]).split(",")[1]
        programLine = _protocol.FileProtoCol.FileSEPATOR.join([str(pcbNum), 'Program', '', '', Program, '', 'T', piceResult, Error])
        AOIMESResList.append(programLine)

        PCBResultLine = _protocol.FileProtoCol.FileSEPATOR.join([str(pcbNum), 'ALL', str(pcbLower), str(pcbUpper), '', '', 'N', piceResult, Error])
        AOIMESResList.append(PCBResultLine)

        pcbNgList = ngList[i]
        if len(pcbNgList)==1:
            AOIBorderLine = _protocol.FileProtoCol.FileSEPATOR.join(
                ['','', '', '','', '', 'T', 'ng', Error])
            AOIMESResList.append(AOIBorderLine)
        else:
            for nn in range(1,len(pcbNgList)):   #遍历添加ng边的结果
                GlueValue = 0
                borderResList = str(pcbNgList[nn]).split(",")
                borderLower = float(borderResList[1])   #当前边下限
                borderUpper = float(borderResList[2])   #当前边上限
                if borderLower>pcbUpper or borderLower<pcbLower:
                    GlueValue = borderLower
                elif borderUpper > pcbUpper or borderUpper < pcbLower:
                    GlueValue = borderUpper
                AOIBorderLine = _protocol.FileProtoCol.FileSEPATOR.join(
                    [str(pcbNum), str(borderResList[0]), '', '', str(GlueValue), '', 'T', 'ng', Error])
                AOIMESResList.append(AOIBorderLine)

        passFlySpeedLine=  _protocol.FileProtoCol.FileSEPATOR.join([str(pcbNum), 'flySpeed', '', '', str(flySpeed), 'mm/s', 'T', piceResult, Error])
        AOIMESResList.append(passFlySpeedLine)

        passFlyLightLine=  _protocol.FileProtoCol.FileSEPATOR.join([str(pcbNum), 'flyLight', '', '', str(flyLight), '', 'T', piceResult, Error])
        AOIMESResList.append(passFlyLightLine)
        # AOIMESResList.append('')

    AOIMESResList.append(_protocol.FileProtoCol.FileEND)  # 文件尾部
    return AOIMESResList

def writeResListToFile(resList,fileName,postfix='.txt',filePath = DotConfig.sysConfig.MESFileSavePath_S["value"]):
    """
    将结果列表写入到指定目录的指定文件中
    :param resList: 结果列表
    :param fileName: 指定文件名
    :param postfix: 文件后缀名
    :param filePath: 指定文件路径
    :return:
    """
    fileName = filePath + os.sep + fileName + postfix

    # 写之前，先检验文件是否存在，存在就删掉
    if os.path.exists(fileName):
        os.remove(fileName)
    # 以写的方式打开文件，如果文件不存在，就自动创建
    file_write_obj = open(fileName,'w',encoding='utf-8')
    for var in resList:
        file_write_obj.writelines(str(var))
        file_write_obj.write('\n')
    file_write_obj.close()
    return fileName


def Test():
    nowTime = datetime.datetime.now()
    strNowTime = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S.%f")
    sTime = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S.%f")[:-3]
    sDate = str(datetime.datetime.now().date())
    print(nowTime)
    print(strNowTime)
    print(sTime)
    print(sDate)

    programL = ";".join(["1", "Program", "", "", "Test", "", "T", "OK",""])
    print(programL)

def TestAOI_old():
    AOIList = None
    AOIPCBList = [1,2,3,6,7,8,9,10]
    barCode = "12345"
    startTime = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S.%f")[:-3]
    time.sleep(2)
    endTime = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S.%f")[:-3]
    flySpeed = 100
    flyLight= 1
    upperLimitList = [10,10,10,10,10,10,10,10]
    lowerLimitList=[150,150,150,150,150,150,150,150]
    AOIResult=["ok","ok","ok","ng","ok","ok","ng","ng",]
    ngList=[[],[],[],[["B","0.7","0.7"],["BL","0.1","0.1"]],[],[],[["T","1.2","152"]],[["R","160","160"],["F","0.7","0.7"]]]
    filename = "Test_AOIMESFile"
    AOIRESList = createAOIMESResListFun_old(AOIList, AOIPCBList, barCode, startTime, endTime, flySpeed, flyLight,
                                        upperLimitList, lowerLimitList, AOIResult, ngList)
    writeResListToFile(AOIRESList, filename, postfix='.txt', filePath="C:/")
    pass

def TestAOI():
    program = "AOITest1"
    AOISeqList = pathList = [{"nIndex": 2, "sType": "AOICHECK", "nPCBNum": 1, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 3, "sType": "AOICHECK", "nPCBNum": 2, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 4, "sType": "AOICHECK", "nPCBNum": 3, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 5, "sType": "AOICHECK", "nPCBNum": 6, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 6, "sType": "AOICHECK", "nPCBNum": 7, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 11, "sType": "AOICHECK", "nPCBNum": 8, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 12, "sType": "AOICHECK", "nPCBNum": 9, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 13, "sType": "AOICHECK", "nPCBNum": 10, "dSpeed": 200, "dZWorkDis": 4.0}]
    AOIPCBList = [1,2,3,6,7,8,9,10]
    barCode = "12345"
    isAllPcbBreak = False
    startTime = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S.%f")[:-3]
    time.sleep(2)
    endTime = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S.%f")[:-3]
    flySpeed = 100
    flyLight= 1
    upperLimitList = [10,10,10,10,10,10,10,10]
    lowerLimitList=[150,150,150,150,150,150,150,150]
    AOIResult=["ok","ok","ok","ng","ok","ok","ng","ng",]
    ngList=[[],[],[],[["B","0.7","0.7"],["BL","0.1","0.1"]],[],[],[["T","1.2","152"]],[["R","160","160"],["F","0.7","0.7"]]]
    filename = "Test_AOIMESFile"
    AOIRESList = createAOIMESResListFun(AOISeqList, AOIPCBList, barCode, startTime, endTime, program,flySpeed, flyLight,
                                        upperLimitList, lowerLimitList,isAllPcbBreak, AOIResult, ngList)
    writeResListToFile(AOIRESList, filename, postfix='.txt', filePath="C:/")
    pass

def TestDot():
    startTime = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S.%f")[:-3]
    time.sleep(2)
    endTime = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S.%f")[:-3]
    pathList = [{"nIndex": 1, "sItem": "PATH", "nPCBNum": 1, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 2, "sItem": "PATH", "nPCBNum": 1, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 3, "sItem": "PATH", "nPCBNum": 2, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 4, "sItem": "PATH", "nPCBNum": 2, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 5, "sItem": "PATH", "nPCBNum": 3, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 6, "sItem": "PATH", "nPCBNum": 3, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 11, "sItem": "PATH", "nPCBNum": 6, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 12, "sItem": "PATH", "nPCBNum": 6, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 13, "sItem": "PATH", "nPCBNum": 7, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 14, "sItem": "PATH", "nPCBNum": 7, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 15, "sItem": "PATH", "nPCBNum": 8, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 16, "sItem": "PATH", "nPCBNum": 8, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 17, "sItem": "PATH", "nPCBNum": 9, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 18, "sItem": "PATH", "nPCBNum": 9, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 19, "sItem": "PATH", "nPCBNum": 10, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 20, "sItem": "PATH", "nPCBNum": 10, "dSpeed": 200, "dZWorkDis": 4.0}]
    DOTPCBList=[1,2,3,6,7,8,9,10]
    isAllPcbBreak = False
    barCode="12345"
    program="Test"
    curTrackT = ["1","33"]
    setValveT = ["1","35"]
    curValveT = ["1","31"]
    singleDotWeight = "0.8"
    DotRadius = "0.465"
    filename = "Test_DotMESFile"  #"Test_DotMESFile_ng"
    DotResList = createDOTMESResListFun(pathList, DOTPCBList, barCode,startTime,endTime, program, curTrackT, setValveT, curValveT,
                                        singleDotWeight,DotRadius,isAllPcbBreak,DotRes="ok", Error="")
    # DotResList = createDOTMESResListFun([], [], barCode,startTime,endTime, program, curTrackT, setValveT, curValveT,
    #                                     singleDotWeight, DotRadius,DotRes="ng", Error="")
    writeResListToFile(DotResList, filename, postfix='.txt', filePath="C:/")

def TestSpeedList():
    DotSpeedList=[]
    pathList = [{"nIndex": 1, "sType": "PATH", "nPCBNum": 1, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 2, "sType": "PATH", "nPCBNum": 1, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 3, "sType": "PATH", "nPCBNum": 2, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 4, "sType": "PATH", "nPCBNum": 2, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 5, "sType": "PATH", "nPCBNum": 3, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 6, "sType": "PATH", "nPCBNum": 3, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 11, "sType": "PATH", "nPCBNum": 6, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 12, "sType": "PATH", "nPCBNum": 6, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 13, "sType": "PATH", "nPCBNum": 7, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 14, "sType": "PATH", "nPCBNum": 7, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 15, "sType": "PATH", "nPCBNum": 8, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 16, "sType": "PATH", "nPCBNum": 8, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 17, "sType": "PATH", "nPCBNum": 9, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 18, "sType": "PATH", "nPCBNum": 9, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 19, "sType": "PATH", "nPCBNum": 10, "dSpeed": 200, "dZWorkDis": 4.0},
                {"nIndex": 20, "sType": "PATH", "nPCBNum": 10, "dSpeed": 200, "dZWorkDis": 4.0}]
    for i in range(10):
        for si in pathList:
            if si['sType'] == 'PATH':
                if str(si['nPCBNum']) == str(i):
                    pathSpeed = [str(si['nIndex']), str(si['dSpeed'])]
                    DotSpeedList.append(pathSpeed)
    print(str(DotSpeedList).replace("'", '"'))
    DotResList = []
    DotResList.append( _protocol.FileProtoCol.FileSEPATOR.join(["ALL",str(DotSpeedList)]))
    writeResListToFile(DotResList, "TestListSave", postfix='.txt', filePath="C:/")

if __name__ == "__main__":
    TestDot()
    TestAOI()
    # Test()
    # TestSpeedList()
    # dic1 = {"nIndex": 1, "sType": "PATH", "nPCBNum": 1, "dSpeed": 200, "dZworkDis": 4.0}
    # dic2 = {"nIndex": 2, "sType": "PATH", "nPCBNum": 1, "dSpeed": 200, "dZworkDis": 4.0}
    # ll = []
    # ll.append(dic1)
    # ll.append(dic2)
    # print(ll)
    # for tei in ll :
    #     print(tei)
    pass

