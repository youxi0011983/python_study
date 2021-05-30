#!/usr/bin/env python3
# coding=utf-8
# 实现文件的服务器的连接，文件上传的下载等功能
# another: iron
# date: 2021/5/28

import paramiko


class UploadFileToServer(object):
    # 所用到的变量
    # host = ''    主机名
    # port = ''    端口号
    # username = ''   用户名
    # password = ''   密码
    # timeout = ''    超时
    # tran = ''       传输
    # chan = ''       渠道
    # try_times = ''   超时次数
    # ssh=             ssh连接

    # 通过域名或ip登录。
    def __init__(self, hostname, username, password, port=22, timeout=30):
        self.hostname = hostname
        # 默认值是22
        self.port = port
        self.username = username
        self.password = password
        # 默认值是30
        self.timeout = timeout
        # transport 和 chanel
        self.tran = ''
        self.chan = ''
        # 连接失败的次数
        self.try_times = 3
        self.ssh = ''

    # 设置内部变量
    def set(self, hostname, username, password, port=22, timeout=30):
        self.hostname = hostname
        # 默认值是22
        self.port = port
        self.username = username
        self.password = password
        # 默认值是30
        self.timeout = timeout
        # transport 和 chanel
        self.tran = ''
        self.chan = ''
        # 连接失败的次数
        self.try_times = 3
        self.ssh = ''

    def get(self):
        return ({'hostname': self.hostname, 'port': self.port, 'username': self.username, 'password': self.password,
                 'timeout': self.timeout, 'tran': self.tran, 'chan': self.chan, 'try_times': self.try_times,
                 'ssh': self.ssh})

    # 连接服务器
    def connect(self):
        # 创建一个ssh对象
        self.ssh = paramiko.SSHClient()
        # 如果之前没有连接郭的ip，会出现Are you sure you want to continue connecting(yes/no)?yes
        # 自动选择yes
        key = paramiko.AutoAddPolicy()
        self.ssh.set_missing_host_key_policy(key)
        try:
            self.ssh.connect(hostname=self.hostname, port=self.port, username=self.username,
                             password=self.password, timeout=self.timeout)
        except Exception as e:
            print(e)
            print("连接超时")
            exit(0)

        print("连接成功")

    # 断开连接
    def close(self):
        if self.ssh != '':
            self.ssh.close()
        if self.tran != '':
            self.tran.close()

    # 执行命令
    def send(self, command):
        # 未完善的功能，需要判断危险的操作，主要是linux服务器的权限设置，比如允许非公里用户删除
        if self.ssh == '':
            self.connect()
        # 执行shell命令，返回的是一个元组
        stdin, stdout, stderr = self.ssh.exec_command(command)
        # 返回shell命令的执行结果
        exec_result = stdout.read().decode('utf-8')
        return exec_result

    # 拉文件到本地,
    # 未实现的功能：远端文件是空，或者没有文件，下载报错暂停不写入本地
    def sftp_get_file(self, localfile, remotefile):
        try:
            self.tran = paramiko.Transport(sock=(self.hostname, self.port))
            self.tran.connect(username=self.username, password=self.password)
            sftp = paramiko.SFTPClient.from_transport(self.tran)
            sftp.get(remotefile, localfile)
            print("下载成功")
        except Exception as e:
            print(e)
            self.close()
            print("=================")

    # 上传文件到服务器
    def sftp_put_file(self, localfile, remotefile):
        try:
            self.tran = paramiko.Transport(sock=(self.hostname, self.port))
            self.tran.connect(username=self.username, password=self.password)
            sftp = paramiko.SFTPClient.from_transport(self.tran)
            sftp.put(localfile, remotefile)
            print("上传成功")
        except Exception as e:
            print(e)
            self.close()
            print("=================")
