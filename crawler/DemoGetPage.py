import re
import urllib.request
import urllib.error
import time


# 模拟成浏览器
headers ="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
opener = urllib.request.build_opener()
opener.addheaders=[("User-Agent",headers)]

# 将opener安装为全局
urllib.request.install_opener(opener)
# 设置一个列表listurl存放文章地址列表
listurl = []


# 自定义函数，功能为使用代理服务器
def use_proxy(proxy_addr, url):
    # 建立异常处理机制
    try:
        proxy = urllib.request.ProxyHandler({'https': proxy_addr})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode("utf-8")
        return data
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        # 若为URLError异常，延时10秒执行
        time.sleep(10)
    except Exception as e:
        print("exception:" + str(e))
        # 若为Exception异常，延时1秒执行
        time.sleep(1)

# 获取所有文章链接
def getlisturl(key, pagestart, pageend, proxy):
    try:
        page = pagestart
        # 编码关键字 key
        keycode = urllib.request.quote(key)
        # 编码 "&page"
        pagecode = urllib.request.quote("&page")
        # 循环爬取各页的文章链接
        for page in range(pagestart, pageend+1):
            # 分别构建各页的url链接，每次循环构建一次
            url = "https://weixin.sogou.com/weixin?query="+keycode+"&_sug_type_=&s_from=input&_sug_=y&type=2&page="+str(page)+"&ie=utf8"
            # 用代理服务器爬取，解决ip被封杀问题
            data = use_proxy(proxy, url)
            # 获取文章链接的正则表达式
            listurlpattern = '<div class="txt-box">.*?(http://.*?)"'
            # 获取每页的所有文章链接并添加到列表listurl中
            listurl.append(re.compile(listurlpattern, re.S).findall(data))
        print(" 共获取到"+str(len(listurl))+"页") # 便于调式
        return listurl

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
            # 若为URLError异常，延时10秒执行
            time.sleep(10)
    except Exception as e:
        print("exception:" + str(e))
        # 若为Exception异常，延时1秒执行
        time.sleep(1)

if __name__ == '__main__':
    key = "物联网"
    proxy = "60.174.189.244:9999"
    proxy2=":"
    pagestart = 1
    pageend = 2
    listurl = getlisturl(key, pagestart, pageend, proxy)