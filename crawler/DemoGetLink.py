import re
import urllib.request
import urllib.error

headers = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"


def getlink(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', headers)]
    # 将opener安装为全局
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    # 根据需求构建好链接表达式
    pattern = '(https?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pattern).findall(data)
    # 去除重复元素
    link = list(set(link))
    return link


if __name__ == '__main__':
    url = "http://blog.csdn.net/"
    # 获取对应网页中包含的链接地址
    linklist = getlink(url)
    # 通过for循环遍历输出打印出来
    for link in linklist:
        print(link[0])
