import urllib.request

if __name__ == '__main__':
    url = "http://www.iqianyue.com"
    headers = ("User-Agent","User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    for i in range(1 , 10):
        try:
            file = urllib.request.urlopen(url, timeout=1)
            data = file.read()
            print(len(data))
        except Exception as e:
            print(str(i)+" 出现异常--> "+str(e))