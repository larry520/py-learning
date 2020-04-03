#  -*- coding:utf-8  -*-


class TcpProtocol():
    DATAHEAD = "#"
    DATAEND = "#"
    SEPARATOR = ";"
    class ReqProtocol():
        partnumReqSerial = "0110"
        statusReqSerial = "1020"

    class RspProtocol():
        partnumRspSerial = "0111"
        statusRspSerial = "1021"

class FileProtoCol():
    FileEND = "##"
    FileSEPATOR = ";"