import re

if __name__ == '__main__':
    pattern = "[a-zA-Z]+://[^\s]*[.com|.cn]"
    string = "<a href='http://www.baidu.com'>百度首页<a>"
    result = re.search(pattern, string)
    print(result)
