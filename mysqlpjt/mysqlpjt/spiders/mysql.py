import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MysqlpjtItem


class MysqlSpider(CrawlSpider):
    name = 'mysql'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/']

    rules = (
        Rule(LinkExtractor(allow=('.*?/[0-9]{4}.[0-9]{2}.[0-9]{2}.doc-.*?shtml'), allow_domains=('sina.com.cn')),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = MysqlpjtItem()
        # 通过xpath表达式提取页面标题
        item["name"] = response.xpath("/html/head/title/text()").extract()
        # 通过xpath表达式提取页面的关键字
        item["keywd"] = response.xpath("/html/head/meta[@name='keywords']/@content").extract()
        return item
