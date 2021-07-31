import urllib.request
import http.cookiejar


URL = "https://www.163.com/dy/article/GFEV1AJS05149JUI.html"
PROXY = {'http': "127.0.0.1:8888"}
PATH = "d:\\code\\crawler\\myweb\\222.html"
HEADERS = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Language": "zh-CN,zh;q=0.8,en-US,q=0.5,en;q=0.3",
           "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" ,
           "Connection": "keep-alive",
            "referer": "http://www.163.com" }

if __name__ == '__main__':
    # 设置cookie
    cjar = http.cookiejar.CookieJar()
    proxy = urllib.request.ProxyHandler(PROXY)
    opener = urllib.request.build_opener(urllib.request.HTTPHandler, urllib.request.HTTPCookieProcessor(cjar))
    # 通过for循环遍历字典，构造出指定格式的headers信息
    headall=[]
    for key,vaule in HEADERS.items():
        item = (key, vaule)
        headall.append(item)
    # 将指定格式的headers信息添加好
    opener.addheaders = headall
    # 将opener安装为全局
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(URL).read()
    filehandle = open(PATH, "wb")
    filehandle.write(data)
    filehandle.close()