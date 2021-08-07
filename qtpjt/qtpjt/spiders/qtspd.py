import scrapy
import re
from ..items import QtpjtItem
from scrapy.http import Request


class QtspdSpider(scrapy.Spider):
    name = 'qtspd'
    allowed_domains = ['58pic.com']
    start_urls = ['http://www.58pic.com/tb/']

    def parse(self, response):
        item = QtpjtItem()
        # 构建提取缩略图网址的正则表达式
        paturl = "(http://pic.qiantucdn.com/58pic/.*?).jpg"
        # 提取对应图片地址
        item['picurl'] = re.compile(paturl).findall(str(response.body))
        # 钩爪出提取图片名的正则表达式，以方便构造出本地的文件名
        patlocal = "http://pic.qiantucdn.com/58pic/.*?/.*?/.*?/(.*?).jppg"
        # 提取互联网中的图片名
        item['picid'] = re.compile(patlocal).findall(str(response.body))
        yield item
        # 通过for循环依次遍历1到200页的图片列表页
        for i in range(1, 201):
            # 构造出下一页图篇列表的网址
            nexturl = "http://www.58pic.com/tb/id-" + str(i) + ".html"
            yield Request(nexturl, callback=self.parse)
