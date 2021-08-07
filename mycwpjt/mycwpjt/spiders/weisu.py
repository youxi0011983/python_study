import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WeisuSpider(CrawlSpider):
    name = 'weisu'
    allowed_domains = ['sohu.com']
    start_urls = ['http://news.sohu.com/']

    rules = (
        # 新闻网页的URL地址类似于：
        # ”http://news.sohu.com.com/20160926/n469167364.shtml
        # 所以可以得到提取的正则表达式为 '.*?/n.*?shtml'
        Rule(LinkExtractor(allow=('.*?/n.*?shtml'), allow_domains=('sohu.com')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        # 根据xpath表达式提取新闻网页中的标题
        item["name"] = response.xpath("/html/head/title/text()").extract()
        # 根据xpath表达式提取当前新闻网页的链接
        item["link"] = response.xpath("//link[@rel='canonical']/@href").extract()
        return item
