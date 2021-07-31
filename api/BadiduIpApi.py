# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# 查询IP地址归属地 Python示例代码
if __name__ == '__main__':
    url = 'http://ipapi.api.bdymkt.com/ip2location/retrieve'

    data = '{\n  \"ip\": \"12.4.12.4\"\n}'
    headers = {

        'Content-Type': 'application/json;charset=UTF-8',
        'X-Bce-Signature': 'AppCode/'
    }
    r = requests.request("POST", url, data=data, headers=headers)
    print(r.content)

