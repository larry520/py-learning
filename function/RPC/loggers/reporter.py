import json
import time
from threading import Thread

import zmq

from loggers import events
from loggers import levels
from tinyrpc.exc import RPCError

FATAL_ERROR = -10001
COMMIT_ERROR = -10002
ZIPPED_FILE_ERROR = -10003
InstantPuddingError = -10004
AMIOK_ERROR = -10005

error_codes_map = {
               FATAL_ERROR: 'fatal error',
               COMMIT_ERROR: 'commit error',
               ZIPPED_FILE_ERROR: 'zipped file error',
               InstantPuddingError: 'InstantPudding error',
               AMIOK_ERROR: 'AMIOK error'
              }

PUB_COMMON = "00000"
PUB_ERROR_HEAD = "10001"
PUB_POS_HEAD = "10002"
PUB_WORK_LINE_HEAD = "10003"
PUB_LOG_HEAD = "10004"
PUB_SYS_STATE_HEAD = "10005"
PUB_ERR_HEAD = "10006"
PUB_IO_HEAD = "10007"
PUB_INFO_HEAD = "10008"
class DotEngineReporter(object):
    def __init__(self,publisher):
        self.publisher = publisher
        self.logReporter = optReporter(PUB_LOG_HEAD, self.publisher)
        self.errReporter = optReporter(PUB_ERR_HEAD, self.publisher)
        self.posReporter = optReporter(PUB_POS_HEAD, self.publisher)
        self.stateReporter = optReporter(PUB_SYS_STATE_HEAD, self.publisher)
        self.workReporter = optReporter(PUB_WORK_LINE_HEAD, self.publisher)
        self.IOReporter = optReporter(PUB_IO_HEAD, self.publisher)
        self.infoReporter = optReporter(PUB_INFO_HEAD, self.publisher)

class ReportDataError(RPCError):
    def __init__(self, msg):
        self.msg = msg

    @classmethod
    def create(cls, event_type, key_error):
        msg = 'Missing Data field in report for event: ' + events.get_name(event_type) + '; ' + key_error.message
        return cls(msg)


class Report(object):

    event = None
    data = None

    def _to_dict(self):
        jdata = dict(event=self.event, data=self.data)
        return jdata

    def serialize(self):
        return json.dumps(self._to_dict())

    def __repr__(self):
        r_str = 'event=' + events.get_name(self.event) + '; data=' + str(self.data)
        return r_str


class ReporterProtocol(object):

    @staticmethod
    def create_report(event_type, **kwargs):
        report = Report()
        report.event = event_type
        try:
            if event_type == events.NO_EVENT:
                report.data = kwargs["data"]
            elif event_type == events.SEQUENCE_START:
                report.data = dict(name=kwargs['name'], version=kwargs['version'])
            elif event_type == events.SEQUENCE_END or event_type == events.UOP_DETECTED:
                r = kwargs['result']
                data = dict(result=r)
                if 'logs' in kwargs:
                    data['logs'] = kwargs['logs']
                else:
                    data['logs'] = ''
                if r == -1:
                    data['error'] = kwargs['error']
                report.data = data
            elif event_type == events.ITEM_START:
                names = ['group', 'GROUP', 'TID', 'tid', 'low', 'LOW',
                         'high', 'HIGH', 'unit', 'UNIT', 'description', 'DESCRIPTION']
                report.data = {k.lower(): v for k, v in kwargs.items() if k in names}
                report.data['to_pdca'] = kwargs['to_pdca']
            elif event_type == events.ITEM_FINISH:
                data = dict(result=kwargs['result'], tid=kwargs['tid'])
                if 'error' in kwargs:
                    data['error'] = kwargs['error']
                    data['value'] = kwargs['value']
                else:
                    data['value'] = kwargs['value']
                report.data = data
                report.data['to_pdca'] = kwargs['to_pdca']
            elif event_type == events.ATTRIBUTE_FOUND:
                data = dict(name=kwargs['name'], value=kwargs['value'])
                report.data = data
            elif event_type == events.REPORT_ERROR_OCCURRED :
                error_code = kwargs['error_code']
                error_msg = error_codes_map[error_code]
                if 'error_msg' in kwargs:
                    error_msg = kwargs['error_msg']
                data = dict(error_code=kwargs['error_code'], error_msg=error_msg, site=kwargs['site'])
                report.data = data
            elif event_type == events.SEQUENCE_LOADED:
                report.data = dict(name=kwargs['name'])
            elif event_type == events.ROBOT_POS_INFO:
                report.data = kwargs['pos']
            elif event_type == events.PATH_LINE_NUM:
                report.data = kwargs['lineNum']
            elif event_type == events.SFR_STEP_RESULT or event_type == events.SFR_END_RESULT\
                    or event_type == events.IO_STATUS:
                report.data = kwargs['data']
            elif event_type == events.SYS_LOG or event_type == events.WORK_LOG:
                report.data = " "+kwargs['data']
            elif event_type == events.SYS_STATE:
                report.data = kwargs['state']
            elif event_type == events.INFO_STATUS:
                report.data = kwargs['info']
            elif event_type == events.VISION_ERROR or event_type == events.MOTION_ERROR:
                report.data = kwargs['error']
            else:
                raise ReportDataError('unknown event_type ' + str(event_type))
        except KeyError as e:
            raise ReportDataError.create(event_type, e)

        return report

    @staticmethod
    def parse_report(report_str):
        report = Report()
        try:
            report_dict = json.loads(report_str)
            report.event = report_dict['event']
            report.data = report_dict['data']
        except Exception as e:
            report.event = events.NO_EVENT
            report.data = report_str
        return report

    @staticmethod
    def is_report(msg):
        if 'data' in msg and 'event' in msg:
            return True
        else:
            return False

import logging
import inspect
class optReporter(object):
    def __init__(self, head_type, publisher):
        self.publisher = publisher
        self.protocol = ReporterProtocol()
        self.head_type = head_type

    def opt_report(self, event_type, id_postfix=None,level =levels.REPORTER ,**kwargs):
        report = self.protocol.create_report(event_type, **kwargs)
        self.publisher.opt_publish(self.head_type, report.serialize(),id_postfix=id_postfix, level=level)
        if self.head_type == PUB_LOG_HEAD:
            location = inspect.stack()[1][1]
            lineNum = inspect.stack()[1][2]
            if event_type == events.SYS_LOG:
                data = ("%s N%s SYS:%s" % (location, lineNum, report.data))
            if event_type == events.WORK_LOG:
                data = ("%s N%s WORK:%s" % (location, lineNum, report.data))
            logging.info(data)

# class Reporter(object):
#
#     def __init__(self, publisher):
#         self.publisher = publisher
#         self.protocol = ReporterProtocol()
#
#     def report(self, event_type, **kwargs):
#         report = self.protocol.create_report(event_type, **kwargs)
#         self.publisher.publish(report.serialize(), level=levels.REPORTER)


# class ReportListener(Thread):
#     def __init__(self, port, url=None):
#         super(ReportListener, self).__init__()
#         ctx = zmq.Context.instance()
#         self.subscriber = ctx.socket(zmq.SUB)
#         if url is None:
#             url = 'tcp://localhost:' + str(port)
#         self.subscriber.connect(url)
#         self.url = url
#         self.subscriber.setsockopt(zmq.SUBSCRIBE, str(zmqports.get_zmq_port("PUB_CHANNEL")))
#         self.receiving = True
#         self.level = levels.REPORTER
#         self.listeners = []
#
#     def run(self):
#         protocol = ReporterProtocol()
#         self.receiving = True
#         print('ready to subscribe to ' + str(self.url))
#         while self.receiving:
#             try:
#                 topic, ts, level, origin, data = self.subscriber.recv_multipart(zmq.NOBLOCK)
#                 if int(level) == self.level:    # process Reporter message only
#                     for listener in self.listeners:
#                         listener.received(protocol.parse_report(data))
#             except zmq.ZMQError:
#                 pass
#             time.sleep(0.02)
#         self.subscriber.setsockopt(zmq.LINGER, 0)
#         self.subscriber.close()
