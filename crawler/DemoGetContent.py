import re
import urllib.request
import urllib.error

headers ="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

def getcontent(url,page):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', headers)]
    # 将opener安装为全局
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode("utf-8")
    # 构建对应用户提取的正则表达式
    userpattern = 'target="_blank" title="(.*?)">'
    # 构建段子内容提取的正则表达式
    contentpattern = '<div class="content">(.*?)</div>'
    # 寻找出所有哦的用户
    uselist = re.compile(userpattern, re.S).findall(data)
    # 寻找出所有的内容
    contentlist = re.compile(contentpattern, re.S).findall(data)
    x = 1
    # 通过for循环遍历段子内容并将内容分别赋给对应的变量
    for content in contentlist:
        content = content.replace("\n", " ")
        # 用字符串作为变量名，先将独赢字符串赋给一个变量
        name = "content"+str(x)
        exec(name+'=content')
        x += 1
    y = 1
    # 通过for循环遍历用户，并输出该用户对应的内容
    for user in uselist:
        name = "content" + str(y)
        print(" 用户"+str(page)+str(y)+"是 ："+user)
        print(" 内容是 ：")
        exec("print("+name+")")
        print("\n")
        y += 1


if __name__ == '__main__':
    for i in range(1,30):
        url = "http://www.qiushibaike.com/8hr/page"+str(i)
        getcontent(url, i)