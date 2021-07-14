import re
if __name__ == '__main__':
    pattern = "yue"  #普通字符作为原子
    string = "http://yum.iqianyue.com"
    result = re.search(pattern, string)
    print(result)