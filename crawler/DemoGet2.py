import urllib.request

if __name__ == '__main__':
    url = "https://www.baidu.com/s?wd="
    keyword = "你好"
    headers ="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    key_code = urllib.request.quote(keyword)
    url_all = url+key_code
    req = urllib.request.Request(url_all)
    req.add_header("User-Agent", headers)
    data = urllib.request.urlopen(req).read()
    fileHandle = open("d:\\code\\crawler\\myweb\\5.html", "wb")
    fileHandle.write(data)
    fileHandle.close()
