import urllib.request

if __name__ == '__main__':
    keyword = "hello"
    url = "https://www.baidu.com/s?wd="+keyword
    headers ="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    req = urllib.request.Request(url)
    req.add_header("User-Agent", headers)
    data = urllib.request.urlopen(req).read()
    fileHandle = open("d:\\code\\crawler\\myweb\\4.html", "wb")
    fileHandle.write(data)
    fileHandle.close()
