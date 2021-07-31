import queue
import re
import urllib.error
import urllib.request
import threading
import time

urlqueue = queue.Queue()
# 模拟成浏览器
headers ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
url = "https://weixin.sogou.com/weixin?query=%E7%89%A9%E8%81%94%E7%BD%91&_sug_type_=&s_from=input&_sug_=y&type=2&page=2&ie=utf8"
opener = urllib.request.build_opener()
opener.addheaders = [("User-Agent", headers)]
# 将opener安装为全局
urllib.request.install_opener(opener)
listurl=[]
PATH = "d:\\code\\crawler\\myweb\\110.html"


def use_proxy(proxy_addr,url):
    try:
        proxy = urllib.request.ProxyHandler({'http':proxy_addr})
        opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('utf-8')
        return data
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print("exception"+str(e))
        time.sleep(1)


# 线程1，专门获取对应网址并发处理为真实网址
class GetURL(threading.Thread):
    def __init__(self,key, pagestart, pageend, proxy, urlqueue, url):
        threading.Thread.__init__(self)
        self.pagestart = pagestart
        self.pageend=pageend
        self.proxy = proxy
        self.urlqueue = urlqueue
        self.key= key
        self.url = url

    def run(self):
        page = self.pagestart
        # 编码关键字key
        keycode = urllib.request.quote(self.key)
        # 编码 “&page”
        pagecode = urllib.request.quote("&page")
        for page in range(self.pagestart, self.pageend+1):
            data = use_proxy(self.proxy, self.url)
            listurlpat = '<div class="txt-box">.*?(http://.*?)"'
            listurl.append(re.compile(listurlpat, re.S).findall(data))
        print("获取到"+str(len(listurl))+"页")
        for i in range(0,len(listurl)):
            # 等一等线程2，合理分配资源
            time.sleep(7)
            for j in range(0,len(listurl[i])):
                try:
                    url = listurl[i][j]
                    # 处理真实的url，
                    url = url.replace("amp;","")
                    print("第"+str(i)+"i"+str(j)+"j次入队")
                    self.urlqueue.put(url)
                    self.urlqueue.task_done()
                except urllib.error.URLError as e:
                    if hasattr(e, "code"):
                        print(e.code)
                    if hasattr(e, "reason"):
                        print(e.reason)
                    time.sleep(10)
                except Exception as e:
                    print("exception" + str(e))
                    time.sleep(1)


# 线程2，与线程1并行执行，从线程1提供的文章网址中依次爬取对应文章信息并处理
class GetContent(threading.Thread):
    def __init__(self, urlqueue, proxy ,url):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue
        self.proxy = proxy
        self.url = url

    def run(self):
        htmlstart = '''
        <!DOCTYPE html>
        <head>
        <title>搜狗微信搜索_订阅号及文章内容独家收录，一搜即达</title>
        </head>
        <body>
        '''
        filehandle = open(PATH,"wb")
        filehandle.write(htmlstart.encode("utf-8"))
        filehandle.close()
        filehandle = open(PATH, "ab")
        i = 1
        while(True):
            try:
                url = self.urlqueue.get()
                data = use_proxy(self.proxy,self.url)
                titlepat = "<title>(.*?)</title>"
                contentpat = 'id="js_content">(.*?)id-"js_sg_bar"'
                title = re.compile(titlepat).findall(data)
                content = re.compile(contentpat,re.S).findall(data)
                thistitle = "此次没有获取到"
                thiscontent = "此次没有获取到"
                if(title!=[]):
                    thistitle=title[0]
                if(content!=[]):
                    thiscontent=content[0]
                dataall ="<p> 标题为："+thistitle+"</p><p>内容为："+thiscontent+"<p><br>"
                filehandle.write(dataall.encode("utf-8"))
                print("第"+str(i)+"个网页处理")
                i+=1
            except urllib.error.URLError as e:
                if hasattr(e, "code"):
                    print(e.code)
                if hasattr(e, "reason"):
                    print(e.reason)
                time.sleep(10)
            except Exception as e:
                print("exception" + str(e))
                time.sleep(1)
        filehandle.close()
        htmlend='''
        </body></html>'''
        filehandle = open(PATH,"ab")
        filehandle.write(htmlend.encode("utf-8"))


# 并行控制程序，若60秒未响应，并且存url的队列未空，则判断未执行成功
class Conrl(threading.Thread):
    def __init__(self, urlqueue):
        threading.Thread.__init__(self)
        self.urlqueue=urlqueue

    def run(self):
        while(True):
            print("程序执行中")
            time.sleep(60)
            if(self.urlqueue.empty()):
                print("程序执行完毕！")
                exit()


if __name__ == '__main__':
    key = "人工只能"
    proxy = "119.6.136.122:80"
    pagestart = 1
    pageend = 2
    # 创建线程1对象，随后启动线程1
    t1 = GetURL(key, pagestart, pageend, proxy, urlqueue, url)
    t1.start()
    # 创建线程2对象，随后启动线程2
    t2 = GetContent(urlqueue, proxy, url)
    t2.start()
    # 创建线程3对象，随后启动线程3
    t3 = Conrl(urlqueue)
    t3.start()



