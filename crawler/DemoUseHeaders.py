import urllib.request

if __name__ == '__main__':
    # url="http://blog.csdn.net/weiwei_pig/aritcle/details/51178226"
    url = "https://blog.csdn.net/weiwei_pig/article/details/69891700?spm=1001.2014.3001.5501"
    req = urllib.request.Request(url)
    req.add_header("User-Agent","User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    data = urllib.request.urlopen(req).read()
    fileHandle = open("d:\\code\\crawler\\myweb\\3.html", "wb")
    fileHandle.write(data)
    fileHandle.close()
