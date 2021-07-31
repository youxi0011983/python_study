import urllib.request
import http.cookiejar


URL = "https://www.163.com/dy/article/GFEV1AJS05149JUI.html"
PROXY = {'http': "127.0.0.1:8888"}
PATH = "d:\\code\\crawler\\myweb\\111.html"
HEADERS = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

if __name__ == '__main__':
    cjar = http.cookiejar.CookieJar()
    # proxy = urllib.request.ProxyHandler(PROXY)
    # opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler, urllib.request.HTTPCookieProcessor(cjar))
    # urllib.request.install_opener(opener)
    req = urllib.request.Request(URL)
    req.add_header("User-Agent", HEADERS)
    data = urllib.request.urlopen(URL).read()
    filehandle = open(PATH, "wb")
    filehandle.write(data)
    filehandle.close()