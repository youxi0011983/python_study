import scrapy
import re
import urllib.request
from ..items import HexunpjtItem
from scrapy.http import Request

HEADERS = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Language": "zh-CN,zh;q=0.8,en-US,q=0.5,en;q=0.3",
           "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
           "Connection": "keep-alive"
           }


class MyhexspiderSpider(scrapy.Spider):
    name = 'myhexspider'
    allowed_domains = ['hexun.com']
    # 通过要爬取的用户的uid，为后续构造爬取网址做准备
    uid = "28826438"

    # start_urls = ['http://hexun.com/']

    def start_requests(self):
        # 首次爬取模拟成浏览器进行
        yield Request("http://" + str(self.uid) + ".blog.hexun.com/p1/default.html", headers=HEADERS)

    def parse(self, response):
        item = HexunpjtItem()
        item['name'] = response.xpath("//span[@class='ArticleSubstanceText']/a/text()").extract()
        item['url'] = response.xpath("//span[@class='ArticleSubstanceText']/a/@href").extract()
        # 接下来需要使用urllib和re模块获取博客的评论数和阅读数
        # 首先提取存储评论数和点击数网址的正则表达式
        pat_one = '<script type="text/javascript" src="(http://click.tool.hexn.com/.*?)">'
        # hcur_one 为存储评论数和点击数网址
        print(pat_one+"\n")
        print(response.body)
        hcur_one = re.compile(pat_one).findall(str(response.body))[0]
        print(hcur_one+"\n")
        # 模拟成浏览器
        opener = urllib.request.build_opener()
        opener.addheaders = [HEADERS]
        # 将opener安装为全局
        urllib.request.install_opener(opener)
        # data为对应博客链表页的所有博文的点击数与评论数数据
        data = urllib.request.urlopen(hcur_one).read()
        # pat_two 为提取文章阅读数的正则表达式
        pat_two = "click\d*?','(\d*>)'"
        # pat_three 为提取文章评论数的正则表达式
        pat_three = "comment\d*?','(\d*>)'"
        # 提取阅读数和评论数数据并分贝赋值给item下的hits和comment
        item["hits"] = re.compile(pat_two).findall(str(data))
        item["comment"] = re.compile(pat_three).findall(str(data))
        yield item
        # 提取博文列表的总页数
        pat_four = "blog.hexun.com/p(.*?)/"
        # 通过正则表达式获取到的数据为一个列表，倒数第二个元素为总页数
        total_data = re.compile(pat_four).findall(str(response.body))
        if (len[total_data] >= 2):
            total_url = total_data[-2]
        else:
            total_url = 1

        # 在实际运行中，下一行print的代码可以注释掉，在调式过程中，可以开启下一行的print代码
        print("一共" + str(total_url) + "页")
        for i in range(2, int(total_url) + 1):
            # 构造下一次要爬取的url，爬取一页报文列表页中的数据
            nexturl = "http://" + str(self.uid) + ".blog.hexun.com/p" + str(i) + "/default.html"
            # 进行下一次的爬取，下一次的爬取仍然模拟浏览器进行
            yield Request(nexturl, callback=self.parse, headers=HEADERS)
