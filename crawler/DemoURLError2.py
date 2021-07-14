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