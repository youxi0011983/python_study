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
    patternTwo = '<img width="220" height="220" data-img="1".+?/>'
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
