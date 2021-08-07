import scrapy
from autopjt.items import AutopjtItem
from scrapy.http import Request


class AutospdSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4002048.html']

    def parse(self, response):
        item = AutopjtItem
        # 通过各Xpath表达式提取商品价格、名称、链接、评论等信息
        item["name"] = response.xpath("//a[@class='pic']/@title").extract()
        item["price"] = response.xpath("//span[@class='price_n']/text()").extract()
        item["link"] = response.xpath("//a[@class='pic']/@href").extract()
        item["comnum"] = response.xpath("//a[@name='P_pl']/text()").extract()

        # 提取完成后返回item
        yield item
        for i in range(1, 3):
            url = "http://category.dangdang.com/pg" + str(i) + "-cid4002048.html"
            # 通过yield返回 Reqest，并指定爬取的网址和回调函数
            # 实现自动爬取
            yield Request(url, callback=self.parse)
