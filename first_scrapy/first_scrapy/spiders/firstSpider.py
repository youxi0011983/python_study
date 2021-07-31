import scrapy
from first_scrapy.items import FirstScrapyItem


class FirstspiderSpider(scrapy.Spider):
    name = 'firstSpider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://slide.news.sina.com.cn/c/slide_1_86058_518824.html',
                  'http://slide.mil.news.sina.com.cn/k/slide_8_193_101155.html/d/1#p=1',
                  ]

    # 重写初始化方法—__init__,并设置参数myurl
    def __init__(self, myurl=None, *args, **kwargs):
        super(FirstspiderSpider, self).__init__(*args,**kwargs)
        # 通过split()将传递进来的参数以“|”为切割符进行分隔，分隔后生成一个列表并赋值给myurllist变量
        myurllist = myurl.split("|")
        # 通过for循环遍历该列表myurllist，并分别输出传进来要爬取的各网址
        for url in myurllist:
            # 输入要爬的网址，对应值为接收到的参数
            print("要爬取的网址为：%s" %url)
        # 将起始网址设置为传进来的参数中各网址组成的列表
        self.start_urls = myurllist

    def parse(self, response):
        item = FirstScrapyItem()
        item["urlname"] = response.xpath("/html/head/title/text()")
        print("以下将显示爬取的网址的标题！")
        print(item["urlname"])

