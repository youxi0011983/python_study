# old_size = os.path.getsize('jar\\asc\\dev\\MEMORY.DMP')
# print (old_size)


import sys
import time
import os
import ftplib
from configparser import SafeConfigParser
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

monitor_dir = {
    'dev': ["jar\\asc\\dev", "jar\\cam\\dev", "jar\\chm\\dev", "jar\\cim\\dev", "jar\\cus\\dev", "jar\\iam\\dev",
            "jar\\web\\dev\\h5", "jar\\web\\dev\\pc"],
    'sit': ["jar\\asc\\sit", "jar\\cam\\sit", "jar\\chm\\sit", "jar\\cim\\sit", "jar\\cus\\sit", "jar\\iam\\sit",
            "jar\\web\\sit\\h5", "jar\\web\\sit\\pc"],
    'uat': ["jar\\asc\\uat", "jar\\cam\\uat", "jar\\chm\\uat", "jar\\cim\\uat", "jar\\cus\\uat", "jar\\iam\\uat",
            "jar\\web\\uat\\h5", "jar\\web\\uat\\pc"]
}


class MyConfig():
    def __init__(self):
        self.myloaded = False
        self.scp = None

    @staticmethod
    def instance():
        if not hasattr(MyConfig, "_instance"):
            MyConfig._instance = MyConfig()
        return MyConfig._instance

    def load_config(self, filename):
        self.scp = SafeConfigParser()
        self.scp.read(filename)
        self.myloaded = True
        return self

    @property
    def loaded(self):
        return self.myloaded

    def get_segment(self, segment_name):
        result = {}
        keys = self.scp.options(segment_name)
        for k in keys:
            result[k] = self.scp.get(segment_name, k)
        return result


class MyFTPClient():
    def __init__(self):
        self.myloaded = False
        self.ftp = None

    @staticmethod
    def instance():
        if not hasattr(MyFTPClient, "_instance"):
            MyFTPClient._instance = MyFTPClient()
        return MyFTPClient._instance

    @property
    def loaded(self):
        return self.myloaded

    def load_config(self, configfile):
        if not MyConfig().instance().loaded:
            MyConfig().instance().load_config(configfile)

        host = MyConfig().instance().get_segment('FTP Config master')['ftp_host']
        self.ftp = ftplib.FTP(host)
        user = MyConfig().instance().get_segment('FTP Config master')['ftp_user']
        passwd = MyConfig().instance().get_segment('FTP Config master')['ftp_passwd']
        ftp_pwd = MyConfig().instance().get_segment('FTP Config master')['ftp_pwd']
        self.ftp.login(user, passwd)
        self.ftp.cwd(ftp_pwd)

    def upload_file(self, file_abs_path):
        command = 'STOR ' + os.path.basename(file_abs_path)
        os.chdir(os.path.dirname(file_abs_path))
        print("FTP command: [%s]" % command)
        try:
            ret = self.ftp.storbinary(command, open(file_abs_path, "rb"))
        except ftplib.error_perm as e:
            print(e.message)
        # except:
        #    print "unknown error."
        #    pass
        print("upload [%s] O.K." % file_abs_path)


class MyFileMonitor(FileSystemEventHandler):
    def on_created(self, event):
        super(MyFileMonitor, self).on_created(event)
        if not event.is_directory:
            print("created name:[%s]" % event.src_path)

    def on_modified(self, event):
        super(MyFileMonitor, self).on_created(event)
        if not event.is_directory:
            print("modified name:[%s]" % event.src_path)
            abs_path = event.src_path
            MyFTPClient().instance().upload_file(abs_path)


def monitor(path):
    event_handler = MyFileMonitor()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    MyConfig.instance().load_config('config.ini')
    MyFTPClient.instance().load_config('config.ini')
    monitor(MyConfig.instance().get_segment('User PC config')['picture_dir'])
