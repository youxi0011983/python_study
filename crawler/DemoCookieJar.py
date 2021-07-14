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


