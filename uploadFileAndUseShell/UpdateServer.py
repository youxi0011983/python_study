#!/usr/bin/env python3
# coding=utf-8
#
# another: iron
# date: 2021/5/28

import time
from watchdog.observers import Observer
from watchdog.events import *
from uploadFileAndUseShell.ManageMysql import MySqlManager
from uploadFileAndUseShell.UploadFileToUpdateProgram import UploadFileToServer
import os

# 本地文件夹
MONITOR_DIR = {
    'dev': ["jar\\asc\\dev", "jar\\cam\\dev", "jar\\chm\\dev", "jar\\cim\\dev", "jar\\cus\\dev", "jar\\iam\\dev",
            "jar\\web\\dev\\h5", "jar\\web\\dev\\pc"],
    'sit': ["jar\\asc\\sit", "jar\\cam\\sit", "jar\\chm\\sit", "jar\\cim\\sit", "jar\\cus\\sit", "jar\\iam\\sit",
            "jar\\web\\sit\\h5", "jar\\web\\sit\\pc"],
    'uat': ["jar\\asc\\uat", "jar\\cam\\uat", "jar\\chm\\uat", "jar\\cim\\uat", "jar\\cus\\uat", "jar\\iam\\uat",
            "jar\\web\\uat\\h5", "jar\\web\\uat\\pc"]
}

REMOTE_DIR = {
    'dev': ["jar/asc/dev", "jar/cam/dev", "jar/chm/dev", "jar/cim/dev", "jar/cus/dev", "jar/iam/dev",
            "jar/web/dev/h5", "jar/web/dev/pc"],
    'sit': ["jar/asc/sit", "jar/cam/sit", "jar/chm/sit", "jar/cim/sit", "jar/cus/sit", "jar/iam/sit",
            "jar/web/sit/h5", "jar/web/sit/pc"],
    'uat': ["jar/asc/uat", "jar/cam/uat", "jar/chm/uat", "jar/cim/uat", "jar/cus/uat", "jar/iam/uat",
            "jar/web/uat/h5", "jar/web/uat/pc"]
}

HOSTS = {
    'dev': {'hostname': 'xiongliang.synology.me', 'username': 'pi', 'password': '229183xl', 'port': 24, 'timeout': 15}

}


# # 获取文件的hash值
# def get_md5(filename):
#     if not os.path.isfile(filename):
#         print(filename + "is not File")
#         return None
#     myhash = hashlib.md5()
#     # python 读权限会被win10管控
#     # with open(filename, "rb") as f:
#     #     while True:
#     #         value = f.read(8096)
#     #         if not value:
#     #             break
#     value = os.path.getsize(filename)
#     myhash.update()
#     return myhash.hexdigest()


# 监控的文件夹是否创建，修改
class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)
        self.file_cache = {}
        self.flag=True

    def on_modified(self, event):
        if event.is_directory:
            return
        # 去除重复的事情
        file_size = os.path.getsize(event.src_path)
        key = (file_size, event.src_path)
        if key in self.file_cache:
            if self.flag:
                self.flag = False
                return
        self.file_cache[key] = True
        print("file modified:{0}".format(event.src_path))

        # 判断服务器
        # remote_dir = ''
        # for server_name in ['dev', 'sit', 'uat']:
        #     for local_dir in MONITOR_DIR[server_name]:
        #         if local_dir in event.src_path
        #             # 要处理下 改成Linux可以处理的路径
        #             remote_dir = local_dir

        # 判断文件大小是否变化,没有发生变化说明文件复制完成。
        old_size = os.path.getsize(event.src_path)
        while True:
            time.sleep(5)
            new_size = os.path.getsize(event.src_path)
            if new_size == old_size:
                break
            old_size = new_size
        self.flag = True
        print("file copy complete")

        # 连接服务器 判断哪个文件夹文件被改变,上传文件
        host = HOSTS['dev']
        upload = UploadFileToServer(hostname=host['hostname'], port=host['port'], username=host['username'],
                                    password=host['password'], timeout=30)
        upload.connect()
        upload.sftp_put_file(event.src_path, "jar/asc/dev/1234")
        print("上传成功")
        # upload.send('')
        upload.close()



if __name__ == "__main__":
    # 验证所有的文件夹都存在
    for server_name in ['dev', 'sit', 'uat']:
        for local_dir in MONITOR_DIR[server_name]:
            result = os.path.exists(local_dir)
            if not result:
                print("error:Missing folder：{0}".format(local_dir))
                exit(1)
    print("All folders are present")

    # 监控所有文件在做响应的处理
    observer = Observer()
    for server_name in ['dev', 'sit', 'uat']:
        for local_dir in MONITOR_DIR[server_name]:
            event_handler = FileEventHandler()
            observer.schedule(event_handler, local_dir, True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
