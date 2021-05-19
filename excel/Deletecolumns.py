# -*- coding : utf-8 -*-
# coding: utf-8

import pandas as pd
import os
import time
import chardet

# 要判断状态的列
ACTIVATE_COLUMN = 'Bug状态'
SETTLE_COLUMN = '解决日期'
CREATE_COLUMN = '创建日期'

# 需要列属于的状态
ACTIVATE_LIST = ['激活']

# 取文件的默认路径
FILE_PATH = './'

# 需要删除的列内容
DELETE_COLUMN = ['Unnamed: 0', '严重程度', '优先级', 'Bug类型', '重现步骤', '截止日期', '抄送给', '指派日期', '解决版本']


def func_file_name(file_path):
    for root, dirs, files in os.walk(file_path):
        for file in files:
            if os.path.splitext(file)[1] == '.csv':
                return file
        print('only support csv format')
        exit(0)


# 处理gpk转换为utf-8
def func_get_encoding(filename_encoding):
    """
    返回文件编码格式
    """
    try:
        with open(filename_encoding, 'rb') as f:
            return chardet.detect(f.read())['encoding']
    except Exception as error:
        print(error)


def func_to_utf8(filename_to_utf8):
    """
    保存为 to_utf-8
    """
    encoding = func_get_encoding(filename_to_utf8)
    ext = os.path.splitext(filename_to_utf8)
    if ext[1] == '.csv':
        if 'gb' in encoding or 'GB' in encoding:
            df_to_utf8 = pd.read_csv(filename_to_utf8, engine='python', encoding='GBK')
        else:
            df_to_utf8 = pd.read_csv(filename_to_utf8, engine='python', encoding='utf-8')
        df_to_utf8.to_excel(ext[0] + '.xlsx')
        return ext[0] + '.xlsx'
    elif ext[1] == '.xls' or ext[1] == '.xlsx':
        if 'gb' in encoding or 'GB' in encoding:
            df_to_utf8 = pd.read_excel(filename_to_utf8, encoding='GBK')
        else:
            df_to_utf8 = pd.read_excel(filename_to_utf8, encoding='utf-8')
        df_to_utf8.to_excel(filename_to_utf8)
        return filename_to_utf8
    else:
        print('only support csv, xls, xlsx format')


# 删除文件不用的列
def func_deleter_columns(file_name_deleter):
    deleter_df = pd.read_excel(file_name_deleter)
    for column in DELETE_COLUMN:
        deleter_df = deleter_df.drop(column, axis=1)
    return deleter_df


# 选择激活内容的行
def func_select_active_line(df_line):
    df_line = df_line[(df_line[ACTIVATE_COLUMN].isin(ACTIVATE_LIST))]
    return df_line


# 选择解决日期今天的行settle
def func_select_settle_today(df_settle):
    data_string = time.strftime("%Y-%m-%d")
    list_str = list(data_string)
    list_str.pop(5)
    data_string = ''.join(list_str)
    df_settle = df_settle[(df_settle[SETTLE_COLUMN].isin([data_string]))]
    return df_settle


# 选择创建日期今天的行
def func_select_create_today(df_create):
    data_string = time.strftime("%Y-%m-%d")
    list_str = list(data_string)
    list_str.pop(5)
    data_string = ''.join(list_str)
    df_create = df_create[(df_create[CREATE_COLUMN].isin([data_string]))]
    return df_create


if __name__ == '__main__':
    # 读取文件名，转换为utf-8的数据
    filename = func_file_name(FILE_PATH)
    filename_xlsx = func_to_utf8(filename)

    # 删除特定的行
    df = func_deleter_columns(filename_xlsx)

    # 筛选出激活的行，存入excel表
    df_activate = func_select_active_line(df)
    df_activate.to_excel(filename + '激活.xlsx')

    # 筛选今日已解决的行，存入excel表
    df_settle_today = func_select_settle_today(df)
    df_settle_today.to_excel(filename + '今日已解决.xlsx')

    # 筛选今日创建的行，存入excel表
    df_create_today = func_select_create_today(df)
    df_create_today.to_excel(filename + '今日创建.xlsx')
