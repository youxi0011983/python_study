import urllib.request

if __name__ == '__main__':
    # 爬取一个网页
    file = urllib.request.urlopen("http://www.baidu.com")
    data = file.read()
    dataLine = file.readline()
    # print(dataLine)
    # print(data)
    # 返回环境相关信息
    print(file.info())
    # 爬取网页的状态码
    print(file.getcode())
    # 爬取网页的URL地址
    print(file.geturl())

    # 将爬取的网页保存在本地
    fileHandle = open("d:\\code\\crawler\\myweb\\1.html", "wb")
    fileHandle.write(data)
    fileHandle.close()

    # 直接将对应的信息写入到本地
    filename = urllib.request.urlretrieve("http://edu.51cto.com", filename="d:\\code\\crawler\\myweb\\2.html")
    # urlretrieve会有缓存信息，清除缓存代码
    urllib.request.urlcleanup()

    # 进行编码
    print(urllib.request.quote("http://www.sina.com.cn"))
    # 进行解码
    print(urllib.request.unquote("http%3A//www.sina.com.cn"))


