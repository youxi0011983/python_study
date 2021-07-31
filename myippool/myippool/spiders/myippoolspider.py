import scrapy
from myippool.items import MyippoolScrapyItem


class MyippoolspiderSpider(scrapy.Spider):
    name = 'myippoolspider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://slide.news.sina.com.cn/c/slide_1_86058_518824.html',
                  'http://slide.mil.news.sina.com.cn/k/slide_8_193_101155.html/d/1#p=1',
                  ]

    # 定义了新属性url2
    urls2=("http://www.jd.com",
           "http://sina.com.cn",
           "http://yum.iqianyue.com",
           )


    # 重写了start_request()方法
    def start_requests(self):
        # 在该方法中将起始网址设置为从新属性urls2中读取
        for url in self.urls2:
            # 调用make_self_from_url()方法生产具体请求并通过yield返回
            yield self.make_requests_from_url(url)

    def parse(self, response):
        item = FirstScrapyItem()
        item["urlname"] = response.xpath("/html/head/title/text()")
        print(item["urlname"])
