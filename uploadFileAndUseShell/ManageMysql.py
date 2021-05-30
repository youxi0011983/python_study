#!/usr/bin/env python3
# coding=utf-8
# 数据库连接查询
# another: iron
# date: 2021/5/28

import pymysql


class MySqlManager(object):

    # 构造函数初始化
    def __init__(self, hostname, username, password, database, port=3306, timeout=30):
        self.hostname = hostname
        # 默认3306
        self.port = port
        self.username = username
        self.password = password
        # 默认30秒
        self.timeout = timeout
        self.database = database
        self.conn = ''
        self.cursor = ''

    # 设置连接信息
    def set(self, hostname, username, password, database, port=3306, timeout=30):
        self.hostname = hostname
        # 默认3306
        self.port = port
        self.username = username
        self.password = password
        # 默认30秒
        self.timeout = timeout
        self.database = database

    # 返回连接信息
    def get(self):
        return ({'hostname': self.hostname, 'port': self.port, 'username': self.username, 'password': self.password,
                 'timeout': self.timeout, 'database': self.database, 'conn': self.conn, 'cursor': self.cursor})

    # 连接数据库
    def conn_mysql(self):
        try:
            self.conn = pymysql.connect(host=self.hostname, user=self.username, password=self.password, port=self.port,
                                        database=self.database, charset="utf8")

            if self.conn != '':
                print("连接成功")
            return self.conn
        except Exception as e:
            print(e)
            self.close()
            print("=================")

    # 断开连接
    def close(self):
        if self.conn != '':
            self.conn.close()
        if self.cursor != '':
            self.cursor.close()

    # 查询数据
    def execute_sql(self, sql):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            self.close()
            print("=================")
