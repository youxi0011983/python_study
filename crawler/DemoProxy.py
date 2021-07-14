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

