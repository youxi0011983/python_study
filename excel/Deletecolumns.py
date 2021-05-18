# -*- coding : utf-8 -*-
# coding: utf-8

import pandas as pd
import os
import time
import chardet
import datetime

# 激活内容列
activateColumn = 'Bug状态'
activateList = ['激活']
settleColumn = '解决日期'
createColumn = '创建日期'

# 读取文件夹内csv的文件名字
filepath = './'


def file_name(file_path):
    for root, dirs, files in os.walk(file_path):
        for file in files:
            if os.path.splitext(file)[1] == '.csv':
                return file


# 处理gpk转换为utf-8
def get_encoding(filename):
    """
    返回文件编码格式
    """
    with open(filename, 'rb') as f:
        return chardet.detect(f.read())['encoding']


def to_utf8(filename):
    """
    保存为 to_utf-8
    """
    encoding = get_encoding(filename)
    ext = os.path.splitext(filename)
    if ext[1] == '.csv':
        if 'gb' in encoding or 'GB' in encoding:
            df = pd.read_csv(filename, engine='python', encoding='GBK')
        else:
            df = pd.read_csv(filename, engine='python', encoding='utf-8')
        df.to_excel(ext[0] + '.xlsx')
        return ext[0] + '.xlsx'
    elif ext[1] == '.xls' or ext[1] == '.xlsx':
        if 'gb' in encoding or 'GB' in encoding:
            df = pd.read_excel(filename, encoding='GBK')
        else:
            df = pd.read_excel(filename, encoding='utf-8')
        df.to_excel(filename)
        return filename
    else:
        print('only support csv, xls, xlsx format')


# 删除文件不用的列
def deleter_columns(file_name):
    columns_list = ['Unnamed: 0', '严重程度', '优先级', 'Bug类型', '重现步骤', '截止日期', '抄送给', '指派日期', '解决版本']

    deleter_df = pd.read_excel(file_name)
    for column in columns_list:
        deleter_df = deleter_df.drop(column, axis=1)
    return deleter_df


# 选择激活内容的行
def select_active_line(df_line):
    df_line = df_line[(df_line[activateColumn].isin(activateList))]
    return df_line


# 选择解决日期今天的行settle
def select_settle_today(df_settle):
    data_string = time.strftime("%Y-%m-%d")
    list_str = list(data_string)
    list_str.pop(5)
    data_string = ''.join(list_str)
    df_settle = df_settle[(df_settle[settleColumn].isin([data_string]))]
    return df_settle


# 选择创建日期今天的行
def select_create_today(df_create):
    data_string = time.strftime("%Y-%m-%d")
    list_str = list(data_string)
    list_str.pop(5)
    data_string = ''.join(list_str)
    df_create = df_create[(df_create[createColumn].isin([data_string]))]
    return df_create


if __name__ == '__main__':
    filename = file_name(filepath)
    filenamexlsx = to_utf8(filename)

    df = deleter_columns(filenamexlsx)

    df_activate = select_active_line(df)
    df_activate.to_excel(filename + '激活.xlsx')

    df_settle_today = select_settle_today(df)
    df_settle_today.to_excel(filename + '今日已解决.xlsx')

    df_create_today = select_create_today(df)
    df_create_today.to_excel(filename + '今日创建.xlsx')
