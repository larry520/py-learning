import os
import sys
from datetime import datetime
if sys.platform == "darwin":
    import pypudding
from publisher import NoOpPublisher


class DUT(object):
    def __init__(self, index):
        self.index = index
        self.sn = ''
        self.running_item = None


class ReportLogger(object):

    index = 0

    @staticmethod
    def next_index():
        ReportLogger.index += 1
        return ReportLogger.index


class FileLogger(ReportLogger):

    def __init__(self, log_folder='/tmp', site_count=6, publisher=NoOpPublisher(), suffix=''):
        super(FileLogger, self).__init__()
        self.log_f = None
        self.log_folder = log_folder
        self.publisher = publisher
        self.site_count = site_count
        self.file_handles = [None for i in range(site_count)]
        self.log_paths = [None for i in range(site_count)]
        self.devices = {i: None for i in range(self.site_count)}
        self.uut_sn = ['' for i in range(self.site_count)]
        if sys.platform == "darwin":
            gh_station = pypudding.IPGHStation()
            self.product = gh_station[pypudding.IP_PRODUCT]
            self.station_type = gh_station[pypudding.IP_STATION_TYPE]
            self.station_id = gh_station[pypudding.IP_STATION_ID]
            self.station_num = gh_station[pypudding.IP_STATION_NUMBER]
        elif sys.platform == "win32":
            self.product = ""
            self.station_type = ""
            self.station_id = ""
            self.station_num = ""

        self.suffix = suffix
        if hasattr(self, 'did_init'):
            func = self.__getattribute__('did_init')
            func()

    def get_log_path(self, site):
        if not self.log_paths:
            return ''
        elif len(self.log_paths) > site:
            return self.log_paths[site] if self.log_paths[site] else ''
        else:
            return self.log_paths[0] if self.log_paths[0] else ''

    def _attach_log(self, site, handle):
        if handle:
            self.file_handles[site] = handle

    def _release_log(self, site):
        log = self.file_handles[site]
        if log and not log.closed:
            log.close()
            self.file_handles[site] = None

    def _close(self):
        for i in range(self.site_count):
            self._release_log(i)

    def write(self, site, data):
        log = self.file_handles[site]
        if log is None:
            return
        log.write(str(data))
        log.flush()

    def on_sequence_start(self, site, data):
        ts = datetime.strftime(datetime.now(), '%m-%d-%H-%M-%S')
        filename = '_'.join([self.product, self.station_type, 'UUT{}'.format(site), ts, self.suffix])
        self.log_paths[site] = os.path.join(self.log_folder, filename)
        log_f = open(self.log_paths[site], 'w+')
        self._release_log(site)
        self._attach_log(site, log_f)
        self.devices[site] = DUT(ReportLogger.next_index())
        if hasattr(self, 'did_sequence_start'):
            func = self.__getattribute__('did_sequence_start')
            func(site, data)

    def on_sequence_end(self, site, data):
        if hasattr(self, 'did_sequence_end'):
            func = self.__getattribute__('did_sequence_end')
            func(site, data)
        self._release_log(site)
