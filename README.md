# 精通Python网络爬虫

## 第一章 什么是网络爬虫

### 1.1、初识网络爬虫

爬虫类型

- 通过网络爬虫（General Purpose Web Crawler）
- 增量式网路爬虫（Incremental Web Crawler）
- 深层网络爬虫（Deep Web Crawler）：需要想办法自动填写好对应的表单，填写表单时深层网络重要任务。

爬虫扩展--聚焦爬虫

- 控制用户交互、初始化爬行器、确定主题、协调各模块之间的工作、控制爬行过程

  ![image-20210708145356550](https://i.loli.net/2021/07/08/do6S7MKIpFiC12H.png)

## 第二章 网络爬虫技术总览

### 2.1、网络爬虫技术总览图

  ![image-20210710112653172](https://i.loli.net/2021/07/10/YGt9rvKMElzOkIx.png)

### 2.2、搜索引擎的核心

![image-20210710115905068](https://i.loli.net/2021/07/10/Vvnp2uhJKoSy3RU.png)

> 索引和检索的区别：检索是一种行为，索引是一种属性

### 2.3、用户爬虫的那些事儿

所谓用户爬虫，指的是专门用来爬取互联网中用户数据的一种爬虫。

## 第三章 网络爬虫实现原理与实现技术

### 3.1、网络爬虫实现原理详解

#### 1、通用网路爬虫

- 获取初始的URL。
- 根据初始URL爬取页面并获得新的URL。
- 将新的URL放到URL队列中。
- 从URL队列中读取新的URL，并依据新的URL爬取网页。
- 满足爬虫系统设置的停止条件时，停止爬取。

![image-20210710121011660](https://i.loli.net/2021/07/10/teE9YhP4aGzsxo6.png)



#### 2、聚焦网络爬虫

- 对爬取目标的定义和描述
- 获取初始的URL
- 根据初始的URL爬取页面，并获得新的URL
- 从新的URL中过略掉与爬取目标无关的链接。
- 将过略后的链接放到URL队列中。
- 从URL队列中，根据搜索算法，确定URL的优先级，并确定下一步要爬取的URL地址。
- 从下一步要爬取的URL地址中，读取新的URL，然后依据新的URL地址爬取网页，并重复上述爬取过程。
- 满足系统中设置的停止条件时，或无法获取新的URL地址时，停止爬行。

![image-20210710122713780](https://i.loli.net/2021/07/10/S9NuABHsCGDFohO.png)

### 3.2、爬行策略

爬行策略主要有深度优先爬行策略、广度优先爬行策略、大站优先策略、反链策略、其他爬行策略。OPIC策略、Partial PageRandk策略

### 3.3、网页更新策略

主要有3种：用户体验策略、历史数据策略、聚类分析策略

### 3.4、网页分析算法

网页分析算法：

1. 基于用户行为的网页分析算法
2. 基于网络拓扑的网页分析算法
   - 基于网页粒度的分析算法：PageRank算法时一种比较典型的基于网页粒度的分析算法。HITS算法也是网页粒度的分析算法
   - 基于网页块粒度的分析算法
   - 基于网站粒度的分析算法
3. 基于网页内容的网页分析算法

### 3.5、身份识别

Robots协议

### 3.6、网络爬虫实现技术

开发爬虫的语言：Python、Java、PHP、Nodes.JS、C++、Go。

### 3.7、实例-metaseeker

metaseeker是一款实用的网站数据采集程序。

官网https://www.gooseeker.com/pro/gooseeker.html



## 第四章 Urllib库与URLError异常处理

### 4.1、什么是Urllib库

Urllib库是python提供的一个用于操作URL的模块。

- Python2.x中使用import urllib2--对应的，Python3.x中会使用import urllib.request, rullib.error
- Python2.x中使用import urllib--对应的，Python3.x中会使用import urllib.request, rullib.error, urllib.parse
- Python2.x中使用import urlparse--对应的，Python3.x中会使用import urllib.parse
- Python2.x中使用import urllib2--对应的，Python3.x中会使用import urllib.request, rullib.error
- Python2.x中使用urllib2.urlopen--对应的，Python3.x中会使用urllib.request.urlopen
- Python2.x中使用urllib2.urlencode--对应的，Python3.x中会使用urllib.parse.urlencode
- Python2.x中使用urllib2.quote--对应的，Python3.x中会使用urllib.request.quote
- Python2.x中使用cookielib.CookieJar--对应的，Python3.x中会使用http.CookieJar
- Python2.x中使用urllib2.Request--对应的，Python3.x中会使用urllib.request.Request

### 4.2、快速使用Urllib爬取网页

~~~python
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
~~~

### 4.3、浏览器的模拟-Headers属性

出现403错误：需要使用Headers中的user-agent字样的一串信息

~~~html
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
~~~

方法：

1. 使用build_opener()修改报头

~~~python
import urllib.request

if __name__ == '__main__':
    # url="http://blog.csdn.net/weiwei_pig/aritcle/details/51178226"
    url = "https://blog.csdn.net/weiwei_pig/article/details/69891700?spm=1001.2014.3001.5501"
    headers = ("User-Agent","User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    data = opener.open(url).read()
    fileHandle = open("d:\\code\\crawler\\myweb\\3.html", "wb")
    fileHandle.write(data)
    fileHandle.close()

~~~

2. 使用add——header()添加报头

~~~python
import urllib.request

if __name__ == '__main__':
    # url="http://blog.csdn.net/weiwei_pig/aritcle/details/51178226"
    url = "https://blog.csdn.net/weiwei_pig/article/details/69891700?spm=1001.2014.3001.5501"
    headers = ("User-Agent","User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    data = opener.open(url).read()
    fileHandle = open("d:\\code\\crawler\\myweb\\3.html", "wb")
    fileHandle.write(data)
    fileHandle.close()

~~~

### 4.4、超时设置

urllib.request.urlopen(要打开的网址, timeout=时间值)

~~~python
import urllib.request

if __name__ == '__main__':
    url = "http://www.iqianyue.com"
    headers = ("User-Agent","User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    for i in range(1 , 10):
        try:
            file = urllib.request.urlopen(url, timeout=1)
            data = file.read()
            print(len(data))
        except Exception as e:
            print(str(i)+" 出现异常--> "+str(e))
~~~

### 4.5、HTTP协议请求实战

HTTP协议请求的主要分为6种类型

1. GET请求

   ~~~python
   import urllib.request
   
   if __name__ == '__main__':
       keyword = "hello"
       url = "http://www.baidu.com/s?wd="+keyword
       headers ="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
       req = urllib.request.Request(url)
       req.add_header("User-Agent", headers)
       data = urllib.request.urlopen(req).read()
       fileHandle = open("d:\\code\\crawler\\myweb\\4.html", "wb")
       fileHandle.write(data)
       fileHandle.close()
   ~~~

2. POST请求实例分析

   - 设置好URL网址
   - 构建表单数据，并使用urllib.parse.urlencode 对数据进行编码处理
   - 创建Request对象，参数包括URL地址和要传递的数据
   - 使用add_header()添加头信息，模拟浏览器进行爬取
   - 使用urllib.request.urlopen()打开对应的Request对象，完成信息传递
   - 后续处理，比如读取网页内容，将内容写入文件等。

### 4.6、代理服务器的设置

~~~python
import urllib.request


def use_proxy(proxy_addr, url):
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data


if __name__ == '__main__':
    proxy_addr = "60.7.30.170:9999"
    # url = "http://www.baidu.com"
    url = "http://www.testingedu.com.cn:8000/"
    data = use_proxy(proxy_addr, url)
    print(len(data))

~~~

### 4.7、DebugLog实战

边运行边打印调用日志，此时需要开启DebugLog

~~~python
import urllib.request

if __name__ == '__main__':
    httphd = urllib.request.HTTPHandler(debuglevel=1)
    httpshd = urllib.request.HTTPSHandler(debuglevel=1)
    opener = urllib.request.build_opener(httphd, httpshd)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen("http://edu.51cto.com")
~~~

### 4.8、异常处理神器--URLError实战

第一个类URLError类，第二个是URLError类的一个子类-HTTPError类

~~~python
import urllib.request
import urllib.error

if __name__ == '__main__':
    # url = "http://163.204.244.8"
    url = "http://blog.csdn.net"
    try:
        urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print(e)
~~~

异常原因

- 连接不上服务器
- 远程URL不存在
- 无网络
- 出发了HTTPError

HTTPError只能处理异常码，不能处理不存在网址，远程URL不存在异常，连接不上服务器

需要用URLError处理

~~~python
import urllib.request
import urllib.error

if __name__ == '__main__':
    url = "http://163.204.244.8"
    # url = "http://blog.csdn.net"
    # url ="https://www.bsssaidu.com"
    try:
        urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print(e.reason)
~~~

优化后的代码

~~~python
import urllib.request
import urllib.error

if __name__ == '__main__':
    url = "http://163.204.244.8"
    # url = "http://blog.csdn.net"
    # url ="https://www.bsssaidu.com"
    try:
        urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.reason)
    except urllib.error.URLError as e:
        print(e.reason)
~~~

~~~python
import urllib.request
import urllib.error

if __name__ == '__main__':
    # url = "http://163.204.244.8"
    # url = "http://blog.csdn.net"
    url ="https://www.bsssaidu.com"
    try:
        urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
~~~

## 第五章 正则表达式

### 5.1、什么是正则表达式

正则表达式就是描述字符串排列的一套规则。

### 5.2、正则表达式基础知识

1. 原子
   - 普通字符作为原子
   - 非打印字符作为原子
   - 通用字符作为原子
   - 原子表
2. 元字符
   - 任意匹配元字符 “.”
   - 边界限制元字符   "^"  "$"
   - 限定符 "*" "?" "+" "{n}" "{n,}" "{n,m}"
   - 模式选择符  "|"
   - 模式单元符  "()"
3. 模式修正 I M L U S
4. 贪婪模式与懒惰模式

### 5.3、正则表达式常见函数

1. re.match()函数
   - 格式re.match(pattern,string,flag) 
2. re.search()函数
3. 全局配置函数 re.compile() 和 findall()  
   - re.complie(pattern).findall(string)
4. re.sub()函数 根据正则表达式替换某个字符串
   - re.sub(pattern,rep,string.max)

### 5.4、常见实例解析

1. 匹配.com或.cn后缀的URL网址

~~~python
import re

if __name__ == '__main__':
    pattern = "[a-zA-Z]+://[^\s]*[.com|.cn]"
    string = "<a href='http://www.baidu.com'>百度首页<a>"
    result = re.search(pattern, string)
    print(result)

~~~

2. 匹配电话号码

~~~python
import re

if __name__ == '__main__':
    pattern = "\d{4}-\d{7}|\d{3}-\d{8}"
    string = "021-434378473847837483"
    result = re.search(pattern, string)
    print(result)

~~~

### 5.5、什么是Cookie

保存网站的状态信息。

### 5.6、Cookiejar实战精析

~~~python
import http.cookiejar
import urllib.request
import urllib.parse
import urllib.error

# 大部分网站登录都又验证码的校验，这种方式不适用
if __name__ == '__main__':
    url = "http://bbs.chinaunix.net/"
    header = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    localpath = ""
    # 使用urlencode编码处理后，再设置为utf-8编码
    postdata = urllib.parse.urlencode({
        "username": "youxi0011983",
        "password": "229183xl"
    }).encode('utf-8')
    # 构建Request对象
    req = urllib.request.Request(url, postdata)
    req.add_header('User-Agent', header)

    # 使用http.cookiejar.CookieJar()创建CookieJar对象
    cjar = http.cookiejar.CookieJar()
    # 使用HTTPCookieProcessor创建cookie处理器，并以其为参数构建opener对象
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
    # 将opener安装为全局
    urllib.request.install_opener(opener)
    try :
        file = opener.open(req)
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.reason)
        exit(1)
    except urllib.error.URLError as e:
        print(e.reason)
        exit(1)

    data = file.read()
    file = open("d:\\code\\crawler\\myweb\\9.html", "wb")
    file.write(data)
    file.close()

~~~

## 第六章 手写python爬虫

### 6.1、图片爬虫实战

~~~python
import re
import urllib.request
import urllib.error

headers ="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# 功能未完成，匹配的内容不对，爬的页面也有问题。思路正确。
def craw(url, page):
    localpath = "d:/code/crawler/image/"
    # htmlPageOne = str(urllib.request.Request(url).add_header("User-Agent", headers))
    req = urllib.request.Request(url)
    req.add_header("User-Agent", headers)
    htmlPageOne = str(urllib.request.urlopen(req).read())
    patternOne = '<div id="J_goodsList".+?<div id="J_scroll_loading" class="notice-loading-more">'
    result = re.compile(patternOne).findall(htmlPageOne)[0]
    # 需要匹配具体地址
    patternTwo = '<img width="220" height="220" data-img="1".+? .'
    imagelist = re.compile(patternTwo).findall(result)
    x = 1
    for imageurl in imagelist:
        imagename = localpath + str(page) + str(x) + ".jpg"
        imageurl = "http://" + imageurl
        try:
            urllib.request.urlretrieve(imageurl, filename=imagename)
        except urllib.error.HTTPError as e:
            print(e.code)
            print(e.reason)
            x += 1
        except urllib.error.URLError as e:
            print(e.reason)
            x += 1
        x += 1


if __name__ == '__main__':
    for i in range(2, 30):
        url = "https://list.jd.com/list.html?cat=9987,653,655&page=" + str(i)
        craw(url, i)

~~~

### 6.2、链接爬虫实战

思路：

1. 确定好要爬取的入口链接
2. 根据需要构建好链接提取的正则表达式
3. 模拟成浏览器并爬取对应网页
4. 根据2 中的正则表达式提取出该网页中包含的链接
5. 过滤掉重复的链接
6. 后续操作。

~~~python
import re
import urllib.request
import urllib.error

headers ="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"


def getlink(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', headers)]
    # 将opener安装为全局
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    # 根据需求构建好链接表达式
    pattern = '(https?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pattern).findall(data)
    #去除重复元素
    link = list(set(link))
    return link

if __name__ == '__main__':
    url = "http://blog.csdn.net/"
    # 获取对应网页中包含的链接地址
    linklist = getlink(url)
    # 通过for循环遍历输出打印出来
    for link in linklist:
        print(link[0])
~~~

### 6.3、糗事百科爬虫实战

1. 分析各页面的网址规律，构造网址变量，并可以通过for循环实现多页内容的爬取。
2. 构建一个自定函数，专门用来实现爬取某个网页上的段子。
3. 通过for循环分别获取多页的各页URL链接，每页分别调用一次getcontent(url,page)函数

~~~python
import re
import urllib.request
import urllib.error

headers ="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

def getcontent(url,page):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', headers)]
    # 将opener安装为全局
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode("utf-8")
    # 构建对应用户提取的正则表达式
    userpattern = 'target="_blank" title="(.*?)">'
    # 构建段子内容提取的正则表达式
    contentpattern = '<div class="content">(.*?)</div>'
    # 寻找出所有哦的用户
    uselist = re.compile(userpattern, re.S).findall(data)
    # 寻找出所有的内容
    contentlist = re.compile(contentpattern, re.S).findall(data)
    x = 1
    # 通过for循环遍历段子内容并将内容分别赋给对应的变量
    for content in contentlist:
        content = content.replace("\n", " ")
        # 用字符串作为变量名，先将独赢字符串赋给一个变量
        name = "content"+str(x)
        exec(name+'=content')
        x += 1
    y = 1
    # 通过for循环遍历用户，并输出该用户对应的内容
    for user in uselist:
        name = "content" + str(y)
        print(" 用户"+str(page)+str(y)+"是 ："+user)
        print(" 内容是 ：")
        exec("print("+name+")")
        print("\n")
        y += 1


if __name__ == '__main__':
    for i in range(1,30):
        url = "http://www.qiushibaike.com/8hr/page"+str(i)
        getcontent(url, i)
~~~

### 6.4、微信爬虫实战

1. 建立3给自定义函数：一个使用代理服务器，一个函数实现获得多个页面的所有文章链接功能，一个函数实现根据文章链接爬取指定标题和内容并写入对应文件中的功能
2. 使用代理服务器爬取指定网站的内容的功能。
3. 要实现获取多个网页的所有文章链接。我们需要对关键字使用urllib.request.quote进行编码
4. 要实现根据文章链接爬取指定标题的内容并写入对应文件中。
5. 代码中如果发生异常，需要进行延时处理。

~~~python
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
~~~

### 6.5、什么是多线程爬虫

多线程举例

~~~python
import threading
import time


class threadingA(threading.Thread):
    def __init__(self):
        # 初始化线程
        threading.Thread.__init__(self)

    def run(self):
        # 该线程要执行的程序内容：
        for i in range(10):
            print("我是线程A" +  str(i))
            time.sleep(1)


class threadingB(threading.Thread):
    def __init__(self):
        # 初始化线程
        threading.Thread.__init__(self)

    def run(self):
        # 该线程要执行的程序内容：
        for i in range(10):
            print("我是线程B" + str(i))
            time.sleep(1)


if __name__ == '__main__':
    t1 = threadingA()
    t1.start()
    t2 = threadingB()
    t2.start()
~~~

**微型爬虫调整思路**

1. 总台规划程序的流程，并规划好各线程的关系与作用
2. 线程1专门获取对应网址处理为真实网址，然后将网址写入队列urlqueue中，该队列专门用来存放具体文章地址。
3. 线程2与线程1并行执行，从线程1提供的文章网址中依次爬取对应文章信息并处理，处理后将我们需要的结果写入对应的本地文件中
4. 线程3主要用于判断程序是否完成。
5. 在正规的项目设计的时候，我们回希望并行执行的线程执行时间相差相近，
6. 建立合理的延时机制，比如在发生异常之后，进行相应的延时处理。
7. 建立合理的异常处理机制。

~~~python
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
        filehandle = open(PATH,"ab")
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
~~~

## 第七章 学会使用Fiddler

### 7.1、什么时Fiddler

Fiddler是一种常见的抓包分析软件。

### 7.2、爬虫与Fiddler的关系

使用Fiddler查看网址的变化规律

### 7.3、Fiddler的基本原理与基本界面

![image-20210722150613516](https://i.loli.net/2021/07/22/C4WFEoHJ8k3ufjT.png)

![image-20210722150636926](https://i.loli.net/2021/07/22/VH7QW15sU8ftvbj.png)

## 第八章 爬虫的浏览器伪装技术

### 8.1、什么是浏览器伪装技术

常见的反爬虫机制主要有：

1. 通过分析用户请求的Headers信息进行反爬虫
2. 通过检查用户行为进行反爬虫
3. 通过动态页面增加爬虫爬取的难度，

### 8.1、浏览器伪装技术准备工作

常见字段：

1. Accept字段
   - Accept字段主要用来表示浏览器能够支持的内容类型
   - text/html表示html文档
   - application/xhtml+xml表示xhtml文档
   - application/xml表示xml文档
   - q代表权重系数，值介于0和1之间
2. Accept-Encoding字段
   - Accept-Encoding字段主要用来表示浏览器支持的压缩编码
   - gzip是压缩编码的一种
   - deflate是一种无损数据压缩算法
3. Accept-Language字段
   - Accept-Language主要用来表示浏览器所支持支持的语言类型
   - zh-CN表示简体中文
   - en-US表示英语（美国）语言
   - en表示英语语言
4. User-Agent字段
   - User-Agent字段主要表示用户代理，服务器可以通过改字段识别出客户端的浏览器类型、浏览器版本号、客户端的操作系统和版本号
   - Mozilla/5.0 表示浏览器名
   - Windows NT6.1；WOW；rv:47.0表示客户端操作系统的对应信息
   - Gecko表示网页排版引擎对应信息
   - firefox自然表示火狐浏览器
5. Connection:keep-alive
   - Connection表示客户端与服务器的连接类型，对应的字段值主要有两种：
     - keep-alive表示持久性连接
     - close表示单方面关闭连接，让连接断开
6. Host:
   - Host字段表示请求的服务器网址是什么
7. Referer
   - Referer字段表示来源网址地址



### 8.3、爬虫的浏览器伪装技术实战

~~~python
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
~~~

## 第九章 爬虫的定向爬取技术

### 9.1、什么是爬虫的定向爬取技术

爬虫的定向爬取技术就是根据设置的主题，对要爬取的网址或网页中的内容进行筛选。

1. 清晰的定义好爬虫的爬取目标，规划好主题
2. 建立好爬取网址的过滤筛选的规则以及内容的过滤筛选
3. 建立好URL排序算法，让爬虫能够明确优先爬取哪些网页，以什么顺序爬取待爬取的网页。

### 9.2、定向爬取的相关步骤与策略

主要步骤：

1. 理清爬取的目的。
2. 设置网址的过滤规则。
3. 设置好内容采集规则。
4. 规划好采集任务。
5. 将采集结果进行相应的修改，处理成我们想要的格式。
6. 对结果进行进一步处理，完成任务。

信息筛选方法策略主要有：

1. 通过正则表达式筛选。
2. 通过xpath表达式筛选。
3. 通过xslt筛选。

### 9.3、定向爬取实战

~~~python
import urllib.request
import http.cookiejar

PROXY = {'http': "127.0.0.1:8888"}
PATH = "d:\\code\\crawler\\myweb\\111.html"
HEADERS = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Language": "zh-CN,zh;q=0.8,en-US,q=0.5,en;q=0.3",
           "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" ,
           "Connection": "keep-alive",
            "referer": "http://www.163.com" }
# 设置视频编号
VID = "4954540180"
# 设置评论起始编号
COMID="1627381897474"
# 构造出真实评论请求网址
# URL = "https://coral.qq.com/article/"+VID+"/commentnum?callback=_article"+VID+"commentnum&_="+COMID
URL = "https://coral.qq.com/article/"+VID+"/comment/v2?callback=_article"+VID+"commentv2&orinum=10&oriorder=o&pageflag=1&cursor=0&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_="+COMID


if __name__ == '__main__':
    # 设置cookie
    cjar = http.cookiejar.CookieJar()
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
~~~

# 框架实现篇

## 第十章 了解python爬虫框架

### 10.1、什么是python爬虫框架

简单来说，就是一些爬虫项目的半成品。

### 10.2、常见的python爬虫框架

python中常见的爬虫框架主要有：

1. Scrapy框架
2. Crawley框架
3. Portia框架
4. newspaper框架
5. python-goose框架

### 10.3、认识Scrapy框架

Scrapy的官网地址是：http://scrapy.org/。

### 10.4、认识Crawley框架

Crawley的官方地址是：http://project.crawley-cloud.com/。

https://pythonhosted.org/crawley/

### 10.5、认识Portia框架

Portia允许没有任何编程基础的用户可视化的爬取网页的爬虫框架。

Portia主页地址：https://github.com/scrapinghub/portia/。

### 10.6、认识newspaper框架

newspaper是一种用来提取新闻、文章以及内容分析的python爬虫框架。

newspaper主页地址：https://github.com/codelucas/newspaper

主要特点：

1. 比较简洁
2. 速度较快
3. 支持多线程
4. 支持十多种语言

### 10.7、认识python-goose框架

Goose是一款用Java写的文章提取工具。

python-goose主页地址 https://github.com/grangier/python-goose

提取如下信息：

1. 文章主体内容
2. 元描述
3. 元标签
4. 文章中的任何YouTube/Vimeo视频
5. 文章中的主要图片

## 第十一章 爬虫利器--Scrapy安装与配置

pip install scrapy 

## 第十二装 开启Scrapy爬虫项目之旅

### 12.1、认识Scrapy项目的目录结构

1. \_\_init\_\_.py文件为项目的初始化文件，主要写的是一些项目初始化信息
2. items.py文件为爬虫项目的数据容器文件，主要用来定义我们要获取的数据
3. pipelines.py文件为爬虫项目的管道文件，主要用来对items里面定义的数据进行进一步的加工与处理
4. setting.py文件为爬虫项目的设置文件，主要为爬虫项目的一些设置信息
5. spiders/\_\_init\_\_.py文件为爬虫项目的中的爬虫部分的初始化文件

### 12.2、用scrapy进行爬虫项目管理

创建一个Scrapy项目

~~~shell
scrapy startproject myfirstpjt
~~~

项目的帮助信息

~~~shell
scrapy startproject -h
~~~

~~~shell
(venv) D:\code\first_scrapy>scrapy startproject -h
Usage
=====
  scrapy startproject <project_name> [project_dir]

Create new project

Options
=======
--help, -h              show this help message and exit

Global Options
--------------
--logfile=FILE          log file. if omitted stderr will be used
--loglevel=LEVEL, -L LEVEL
                        log level (default: DEBUG)
--nolog                 disable logging completely
--profile=FILE          write python cProfile stats to FILE
--pidfile=FILE          write process ID to FILE
--set=NAME=VALUE, -s NAME=VALUE
                        set/override setting (may be repeated)

~~~

--logfile=FILE主要是指定日志文件

设置日志等级

~~~shell
scrapy startproject --loglevel=DEBUG 
~~~

不输入日志

~~~shell
scrapy startproject --nolog
~~~

### 12.3、常用工具命令

一种全局命令、一种项目命令

1. 全局命令

   - scrapy -h
   - fetch主要用来显示爬取的过程: --headers 显示头信息 ： scrapy fetch --headers --nolog http://www.b
   - runspider命令直接运行一个爬虫文件。
   - setting命令查看scrapy对应配置信息
   - shell命令可以启动scrapy的交互终端
   - startproject 开始一个项目
   - version命令查看scrapy的版本相关信息
   - view命令实现下载某个网页并用浏览器查看

2. 项目命令

   - bench命令可以测试本地硬件的性能

   - genspider创建scrapy爬虫文件

   - check命令对某个爬虫文件进行合同检查

   - crawl启动某个爬虫

   - List命令，可以列出当前可使用的爬虫文件

   - edit可以直接打开编辑器对爬虫文件编辑

   - parse命令可以实现获取指定的URL网址，并使用对应的爬虫文件进行处理和分析

     - |      参数       |                 含义              |
       | :-------------: | -------------------------------- |
       | --spider=SPIDER | 强制指某个爬虫文件spider进行处理 |
       | -a NAME = VALUE | 设置spider的参数，可能会重复     |
       |   --pipelines   | 通过pipelines来处理items         |
       |    --nolinks    | 不展示提取到的连接信息           |
       |    --noitems    | 不展示得到的items                |
       |   --nocolour    | 输出结果颜色不高亮               |
       | --rules,r | 使用CrawlSpider规则去处理回调函数 |
       | --callback=CALLBACK,-c CALLBACK | 指定spider中用于处理返回的响应的回调函数 |
       | --depth=DEPTH,-d DEPTH | 设置爬行深度，默认深度为1 |
       | --verbose,-v | 显示每层的详细信息 |
     



### 12.4、实战:Items编写

~~~python
import scrapy


class FirstScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
   urlname = scrapy.Field()
   urlkey = scrapy.Field()
   urlcr = scrapy.Field()
   urladdr = scrapy.Field()
~~~

### 12.5、实战：Spider的编写

~~~python
import scrapy


class FirstspiderSpider(scrapy.Spider):
    name = 'firstSpider'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://iqianyue.com/']

    def parse(self, response):
        pass

~~~

name属性代表爬虫的名称。所以此爬虫名称为“first Spider”

allowed_domains代表的允许爬行的域名，如果启动了OffsiteMiddleware，非允许的域名对应的网址则会自动过滤掉，不再跟进。

start_urls属性代表的是爬行的起始网址

parse方式，是处理Scrapy爬虫爬行的网页响应的默认方法。对响应进行处理并放回处理后的结果，同时改方法也复制链接的跟进

| 名称                           | 属性or方法 | 含义                                                         |
| ------------------------------ | ---------- | ------------------------------------------------------------ |
| start_requests()               | 方法       | 该方法会默认读取start_urls属性（当然可以自定义）中的定义的网址，为每一个网址生成一个Request请求对象，并放回可迭代对象 |
| make_requests_from_url(url)    | 方法       | 该方法会被start_requests()调用，该方法负责实现生成Request请求对象 |
| closed(reason)                 | 方法       | 关闭Spider时，该方法会被调用                                 |
| log(message[,level,component]) | 方法       | 使用该方法可以实现再Spider中添加log                          |
| \_\_init\_\_()                     | 方法       | 该方法主要负责爬虫的初始化，为构造函数 |

~~~python
import scrapy
from first_scrapy.items import FirstScrapyItem


class FirstspiderSpider(scrapy.Spider):
    name = 'firstSpider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://slide.news.sina.com.cn/c/slide_1_86058_518824.html',
                  'http://slide.mil.news.sina.com.cn/k/slide_8_193_101155.html/d/1#p=1',
                  ]

    # 定义了新属性url2
    urls2=("http://www.jd.com",
           "http://sina.com.cn",
           "http://yum.iqianyue.com",
           )


    # 重写了start_request()方法
    def start_requests(self):
        # 在该方法中将起始网址设置为从新属性urls2中读取
        for url in self.urls2:
            # 调用make_self_from_url()方法生产具体请求并通过yield返回
            yield self.make_requests_from_url(url)

    def parse(self, response):
        item = FirstScrapyItem()
        item["urlname"] = response.xpath("/html/head/title/text()")
        print(item["urlname"])

~~~

### 12.6、xpath基础

1. //提取某个标签的所有信息，例如//p出现多个\<p\>标签
2. 获取所有属性X的值为Y的\<Z\>标签, "//Z[@X="Y"]"

### 12.7、Spider类参数传递

spider类还可以通过-a选项实现参数的传递

~~~python
import scrapy
from first_scrapy.items import FirstScrapyItem


class FirstspiderSpider(scrapy.Spider):
    name = 'firstSpider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://slide.news.sina.com.cn/c/slide_1_86058_518824.html',
                  'http://slide.mil.news.sina.com.cn/k/slide_8_193_101155.html/d/1#p=1',
                  ]

    # 重写初始化方法—__init__,并设置参数myurl
    def __init__(self, myurl=None, *args, **kwargs):
        super(FirstspiderSpider, self).__init__(*args,**kwargs)
        # 输入要爬的网址，对应值为接收到的参数
        print("要爬取的网址为：%s" %myurl)
        # 重新定义start_urls属性，属性值为传进来的参数值
        self.start_urls = ["%s" %myurl]

    def parse(self, response):
        item = FirstScrapyItem()
        item["urlname"] = response.xpath("/html/head/title/text()")
        print("以下将显示爬取的网址的标题！")
        print(item["urlname"])
~~~

如何通过传递参数的方式爬取多个网址

~~~python
import scrapy
from first_scrapy.items import FirstScrapyItem


class FirstspiderSpider(scrapy.Spider):
    name = 'firstSpider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://slide.news.sina.com.cn/c/slide_1_86058_518824.html',
                  'http://slide.mil.news.sina.com.cn/k/slide_8_193_101155.html/d/1#p=1',
                  ]

    # 重写初始化方法—__init__,并设置参数myurl
    def __init__(self, myurl=None, *args, **kwargs):
        super(FirstspiderSpider, self).__init__(*args,**kwargs)
        # 通过split()将传递进来的参数以“|”为切割符进行分隔，分隔后生成一个列表并赋值给myurllist变量
        myurllist = myurl.split("|")
        # 通过for循环遍历该列表myurllist，并分别输出传进来要爬取的各网址
        for url in myurllist:
            # 输入要爬的网址，对应值为接收到的参数
            print("要爬取的网址为：%s" %url)
        # 将起始网址设置为传进来的参数中各网址组成的列表
        self.start_urls = myurllist

    def parse(self, response):
        item = FirstScrapyItem()
        item["urlname"] = response.xpath("/html/head/title/text()")
        print("以下将显示爬取的网址的标题！")
        print(item["urlname"])
~~~

### 12.8、用XMLFeedSpider来分析XML源

Scrapy通过XMLFeedSpider来爬XML文件。

~~~shell
scrapy genspider -t xmlfeed myxmlspider sina.com.cn
~~~

| 名称                              | 属性or方法 | 含义                                                         |
| --------------------------------- | ---------- | ------------------------------------------------------------ |
| namespaces                        | 属性       | 以列表的形式存在，主要定义在文档中会被蜘蛛处理的可用的命名空间 |
| adapt_response(response)          | 方法       | 该方法主要在spider分析响应（Response）前被调用               |
| process_results(response,results) | 方法       | 该方法主要在spider返回结果时被调用，主要对结果在返回前进行最后处理 |

~~~python
# -*- coding utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem


class MyxmlspiderSpider(XMLFeedSpider):
    name = 'myxmlspider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/rss/1361074815.xml']
    # iterator 属性设置的是使用那个迭代器，默认值"iternodes"
    iterator = 'iternodes' # you can change this; see the docs
    # itertag 属性主要用来设置开始迭代的节点。
    itertag = 'item' # change it accordingly

    # 在节点与所提供的标签名相符合的时候会被调用
    def parse_node(self, response, selector):
        item = MyxmlItem()
        # 利用xpath表达式将对应的信息提取出来，并存储到对应的item中
        item['title'] = node.xpath("/rss/channel/item/title/text()").extract()
        item['link'] = node.xpath("/rss/channel/item/link/text()").extract()
        item['author'] = node.xpath("/rss/channel/item/author/text()").extract()
        # 通过for循环以此表里出提取出来存在item中的信息并输出
        for j in range(len(item['title'])):
            print("第"+str(j+1)+"篇文章")
            print("标题时：")
            print(item['title'][j])
            print("对应的链接是：")
            print(item['link'][j])
            print("对应的作者是：")
            print(item['author'][j])
            print("--------------------------------")
        return item
~~~

### 12.9、学会使用CSVFeedSpider

~~~python
from scrapy.spiders import CSVFeedSpider
from myscv.items import MycsvItem


class MycsvspiderSpider(CSVFeedSpider):
    name = 'mycsvspider'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/feed.csv']
    # headers = ['id', 'name', 'description', 'image_link']
    # delimiter = '\t'
    # 定义headers
    headers = ['name', 'sex', 'addr', 'email']
    # 定义间隔符
    delimiter = ','

    # Do any adaptations you need here
    # def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = MycsvItem()
        # 提取各行的name这一列的信息
        i['name'] = row['name'].encode()
        # 提取各行的sex这一列的信息
        i['sex'] = row['sex'].encode()
        # 进行信息输出
        print("名字是：")
        print(i['name'])
        print("性别是：")
        print(i['sex'])
        # 输出完一个记录对应列的信息后，输出一个间隔符，显示起来方便观察
        print("--------------------")
        return i
~~~

### 12.10、Scrapy爬虫多开技能

两种方法实现：

1. 使用CrawProcess实现：官方文档详细介绍http://doc.scrapy.org/en/latest/topics/practices.html
2. 使用修改craw源码+自定义命令的方式实现

crawl命令的源码在scarpy官方github项目中找到 http://github.com/scrapy/scrapy/blob/master/scrapy/commands/crawl.py

### 12.11、避免被禁止

在scrapy项目中，主要可以通过以下方法来避免被禁止：

1. 禁止Cookie；
   - 通过禁止本地Cookie信息让对方网站无法识别出我们会话信息。
   - 设置settings.py文件中的Disable cookies
   -  ![image-20210731230125638](https://i.loli.net/2021/07/31/tWoDZw8CXYSJfId.png)
   
2. 设置下载延时；

   - 设置settings.py文件中的DOWNLOAD_DELAY 
   - ![image-20210731230733662](https://i.loli.net/2021/07/31/7TcKVz1Y2apIxhj.png)

3. 使用IP池；

   - 设置IP池

   - ~~~python
     scrapy.contracts.Downloadermiddleware.httpproxy // 没有这个中间件
     ~~~

4. 使用用户代理池；

   - 用户代理（User-Agent）信息，通过建立代理池，防止禁用
   - UserAgentMiddleware中间件类型

5. 其他方法，比如进行分布式爬取等

   - 谷歌Cache、
   - 分布爬行等方法。scrapinghub旗下的框架进行 http://scrapinghub.com/crawlera/

## 第十三章 Scrapy核心构架

### 13.1、初始Scrapy架构

Scarpy中的组件主要包括：

1. Scrapy引擎
2. 调度器
3. 下载器
4. 下载中间件
5. 蜘蛛也叫爬虫
6. 爬虫中间件
7. 实体管道

![image-20210731234442273](https://i.loli.net/2021/07/31/M4fQWNs18BSPoI2.png)

![image-20210731234527770](https://i.loli.net/2021/07/31/fvSDdPMTxejtGys.png)



### 13.2、常用的Scrapy组件详解

1. Scrapy引擎
   - 负责控制整个数据处理流程，以及触发一些事务处理。
2. 调度器
   - 主要实现存储待爬取的网址，并确定这些网址的优先级，决定下一次爬取哪个网址等。
3. 下载器
   - 主要实现对网络上要爬取的网页资源进行高速下载。
4. 下载中间件
   - 处理下载器和Scrapy引擎之间的一个特定的组件，主要用于下载器和Scrapy引擎之间的通信进行处理。
5. 蜘蛛
   - 该组件时Scrapy框架中爬虫实现的核心。
6. 爬虫中间件
   - 处理爬虫和Scrap引擎之间通信的一个特定组件
7. 实体管道
   - 主要用于接收从蜘蛛组件中提取出来的项目，接收后，会对这些item进行对应的处理，常见处理有：清洗、验证、存储到数据库中等。

### 13.3、Scrapy工作流

组件的具体作用有哪些

![image-20210731235559550](https://i.loli.net/2021/07/31/NADdRP3FZQBGsJr.png)

![image-20210731234545379](https://i.loli.net/2021/07/31/4fQe6mJFjBdroS3.png)

每一个过程的具体含义：

1. 主要将下一次要爬取的网址传递给Scrapy引擎。
2. Scrapy引擎主要将网址传递给下载中间件
3. 下载中间件接收到Scrapy引擎传过来网址后，传递给下载器。
4. 下载器收到对应的下载的网址，会对互联网中对应的网址发送request请求
5. 互联网接收到request请求之后，会有响应的response。
6. 下载器接收到响应之后，即完成对应网页的下载，
7. 下载中间件接收到对应响应之后，会与Scrapy引擎进行通信，将对应的reponse响应传递给Scrapy引擎
8. scrapy引擎接收到response响应之后，将response响应信息传递给爬虫中间件
9. 爬虫中间件接收到对应响应之后，会将响应传递给对应爬虫处理
10. 爬出进行处理之后，大致会有两方面的信息：提取出来的数据和新的请求信息
11. 爬虫中间件接收到对应信息后，会将对应信息传递到Scrapy引擎
12. Scrapy引擎接收到爬虫处理之后的信息会同时和实体管道做进一步处理。



## 第十四章 Scrapy中文输出与存储

### 14.1、Scrapy的中文输出

主要时2.x中文输出不显示，

### 14.2、Scrapy的中文存储

### 14.3、输出中文到JSON文件

json文件也会有中文不显示，显示编码问题

~~~python
codecs.open("d:/python/mydata.json","wb",,encoding="utf-8")
~~~

## 第十五章 编写自动爬取网页的爬虫

### 15.1、实战：items的编写

~~~python
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AutopjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 商品名称
    name = scrapy.Field()
    # 存储商品价格
    price = scrapy.Field()
    # 商品链接
    link = scrapy.Field()
    # 商品评论数
    comnum = scrapy.Field()

~~~

### 15.2、pipelines的编写

~~~python
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import codecs
import json


class AutopjtPipeline:
    def __init__(self):
        # 打开mydata。json文件
        self.file = codecs.open("d:/code/autopjt/mydata.json", "wb", encoding="utf-8")

    def process_item(self, item, spider):
        i = json.dumps(dict(item),ensure_ascii=False)
        # 每条数据后加上踢换行
        line = i +'\n'
        # 数据写入到 mydata.json文件中
        self.file.write(line)
        return item

    def close_spider(self,spider):
        # 关闭 mydata.json文件
        self.file.close()
~~~

### 15.3、settings编写

### 15.4、自动爬虫编写实战

名称 xpath表达式为：”//a[@class='pic']/@title"

~~~python
import scrapy
from autopjt.items import AutopjtItem
from scrapy.http import Request


class AutospdSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4002048.html']

    def parse(self, response):
        item = AutopjtItem
        # 通过各Xpath表达式提取商品价格、名称、链接、评论等信息
        item["name"] = response.xpath("//a[@class='pic']/@title").extract()
        item["price"] = response.xpath("//span[@class='price_n']/text()").extract()
        item["link"] = response.xpath("//a[@class='pic']/@href").extract()
        item["comnum"] = response.xpath("//a[@name='P_pl']/text()").extract()

        # 提取完成后返回item
        yield item
        for i in range(1, 3):
            url = "http://category.dangdang.com/pg" + str(i) + "-cid4002048.html"
            # 通过yield返回 Reqest，并指定爬取的网址和回调函数
            # 实现自动爬取
            yield Request(url, callback=self.parse)

~~~

## 第十六章 CrawlSpider

### 16.1、初识CrawlSpider

创建一个自动爬虫

~~~shell
scrapy startproject mycwpjt
~~~

爬虫的具体内容

~~~python
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WeisuSpider(CrawlSpider):
    name = 'weisu'
    allowed_domains = ['sohu.com']
    start_urls = ['http://sohu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
~~~

### 16.2、链接提取器

~~~python
 rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )
~~~

| 参数名          | 参数含义                                                     |
| --------------- | ------------------------------------------------------------ |
| allow           | 提取复核对应正则表达式链接                                   |
| deny            | 不提取复核对应正则表达式链接                                 |
| restrict_xpaths | 使用xpath表达式与allow共同作用提取出同时符合对应xpath表达式和对应正则表达式的链接 |
| allow_domains   | 允许提取的域名，比如我们想只提取莫格域名下的链接时会用到     |
| deny_domains    | 禁止提取的域名，比如我们需要限制一定不提取某个域名下的链接时会用到 |

我们想要提取有".shtml"字符串的链接，可以将rules规则设置为如下

~~~python
 rules = (
        Rule(LinkExtractor(allow=('.shtml')), callback='parse_item', follow=True),
    )
~~~

限制只是搜索搜狐的链接。

~~~python
 rules = (
        Rule(LinkExtractor(allow=('.shtml')), allow_domain=(sohu.com), callback='parse_item', follow=True),
    )
~~~

### 16.3、实战：CrawlSpider实例

CrawlSpider工作流：

![image-20210806084814834](https://i.loli.net/2021/08/06/OtrKEjhnMbqL6u4.png)

~~~python
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WeisuSpider(CrawlSpider):
    name = 'weisu'
    allowed_domains = ['sohu.com']
    start_urls = ['http://news.sohu.com/']

    rules = (
        # 新闻网页的URL地址类似于：
        # ”http://news.sohu.com.com/20160926/n469167364.shtml
        # 所以可以得到提取的正则表达式为 '.*?/n.*?shtml'
        Rule(LinkExtractor(allow=('.*?/n.*?shtml'), allow_domains=('sohu.com')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        # 根据xpath表达式提取新闻网页中的标题
        item["name"] = response.xpath("/html/head/title/text()").extract()
        # 根据xpath表达式提取当前新闻网页的链接
        item["link"] = response.xpath("//link[@rel='canonical']/@href").extract()
        return item

~~~

我们还可以在链接提取器LinkExtractor中通过restrict_xpaths参数设置一个xpath表达式于allow参数中设置的正则表达式共同来实现链接的过滤和提取

CrawlSpider和之前自动爬虫的区别：

1. CrawlSpider与第15章中学习的自动爬虫实现原理不同，一个时链接关系依次自动爬取，另外一个时规律使用循环自动爬取
2. 之前的自动爬取网页适合有规律的页面，使用循环遍历比较方便
3. CrawlSpider爬取可以适合无规律的url网页自动爬取任务
4. CrawlSpider更适合做通用爬虫

## 第十七章 Scrapy高级应用

### 17.1、如何在python3中操作数据库

安装mysql模块

~~~shell
pip install pymysql3
~~~

代码

~~~python
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MysqlpjtItem


class MysqlSpider(CrawlSpider):
    name = 'mysql'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/']

    rules = (
        Rule(LinkExtractor(allow=('.*?/[0-9]{4}.[0-9]{2}.[0-9]{2}.doc-.*?shtml'), allow_domains=('sina.com.cn')),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = MysqlpjtItem()
        # 通过xpath表达式提取页面标题
        item["name"] = response.xpath("/html/head/title/text()").extract()
        # 通过xpath表达式提取页面的关键字
        item["keywd"] = response.xpath("/html/head/meta[@name='keywords']/@content").extract()
        return item

~~~

## 第十八章 项目实战

### 18.1、博客类爬虫项目功能分析

实现功能：

1. 爬取博客中任意一个用户的所有博文信息
2. 将博文的文章名、文章URL、文章点击数、文章评论数等信息提取出来
3. 将提取出来的文章名、文章URL、文章点击数、文章评论数等信息自动写入MySQL数据库中存储

~~~python
import scrapy
import re
import urllib.request
from ..items import HexunpjtItem
from scrapy.http import Request

HEADERS = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Language": "zh-CN,zh;q=0.8,en-US,q=0.5,en;q=0.3",
           "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
           "Connection": "keep-alive"
           }


class MyhexspiderSpider(scrapy.Spider):
    name = 'myhexspider'
    allowed_domains = ['hexun.com']
    # 通过要爬取的用户的uid，为后续构造爬取网址做准备
    uid = "28826438"

    # start_urls = ['http://hexun.com/']

    def start_requests(self):
        # 首次爬取模拟成浏览器进行
        yield Request("http://" + str(self.uid) + ".blog.hexun.com/p1/default.html", headers=HEADERS)

    def parse(self, response):
        item = HexunpjtItem()
        item['name'] = response.xpath("//span[@class='ArticleSubstanceText']/a/text()").extract()
        item['url'] = response.xpath("//span[@class='ArticleSubstanceText']/a/@href").extract()
        # 接下来需要使用urllib和re模块获取博客的评论数和阅读数
        # 首先提取存储评论数和点击数网址的正则表达式
        pat_one = '<script type="text/javascript" src="(http://click.tool.hexn.com/.*?)">'
        # hcur_one 为存储评论数和点击数网址
        print(pat_one+"\n")
        print(response.body)
        hcur_one = re.compile(pat_one).findall(str(response.body))[0]
        print(hcur_one+"\n")
        # 模拟成浏览器
        opener = urllib.request.build_opener()
        opener.addheaders = [HEADERS]
        # 将opener安装为全局
        urllib.request.install_opener(opener)
        # data为对应博客链表页的所有博文的点击数与评论数数据
        data = urllib.request.urlopen(hcur_one).read()
        # pat_two 为提取文章阅读数的正则表达式
        pat_two = "click\d*?','(\d*>)'"
        # pat_three 为提取文章评论数的正则表达式
        pat_three = "comment\d*?','(\d*>)'"
        # 提取阅读数和评论数数据并分贝赋值给item下的hits和comment
        item["hits"] = re.compile(pat_two).findall(str(data))
        item["comment"] = re.compile(pat_three).findall(str(data))
        yield item
        # 提取博文列表的总页数
        pat_four = "blog.hexun.com/p(.*?)/"
        # 通过正则表达式获取到的数据为一个列表，倒数第二个元素为总页数
        total_data = re.compile(pat_four).findall(str(response.body))
        if (len[total_data] >= 2):
            total_url = total_data[-2]
        else:
            total_url = 1

        # 在实际运行中，下一行print的代码可以注释掉，在调式过程中，可以开启下一行的print代码
        print("一共" + str(total_url) + "页")
        for i in range(2, int(total_url) + 1):
            # 构造下一次要爬取的url，爬取一页报文列表页中的数据
            nexturl = "http://" + str(self.uid) + ".blog.hexun.com/p" + str(i) + "/default.html"
            # 进行下一次的爬取，下一次的爬取仍然模拟浏览器进行
            yield Request(nexturl, callback=self.parse, headers=HEADERS)
~~~
