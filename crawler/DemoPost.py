import urllib.request
import urllib.parse

if __name__ == '__main__':
    url = "http://www.testingedu.com.cn:8000/"
    headers ="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    postdata = urllib.parse.urlencode({"name": "cesjdsjad", "pass": "addjkajd"}).encode('utf-8')
    req = urllib.request.Request(url, postdata)
    req.add_header('User-Agent', headers)
    data = urllib.request.urlopen(req).read()
    fileHandle = open("d:\\code\\crawler\\myweb\\7.html", "wb")
    fileHandle.write(data)
    fileHandle.close()

