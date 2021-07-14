import urllib.request
import urllib.parse
import urllib.error

if __name__ == '__main__':
    url = "http://account.chinaunix.net/login/"
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
    # 登录并爬取对应网页
    try:
        data = urllib.request.urlopen(req).read()
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.reason)
        exit(1)
    except urllib.error.URLError as e:
        print(e.reason)
        exit(1)
    filehandle = open("d:\\code\\crawler\\myweb\\8.html", "wb")
    filehandle.write(data)
    filehandle.close()






