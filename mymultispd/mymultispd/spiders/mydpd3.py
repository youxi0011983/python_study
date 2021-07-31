import scrapy


class Mydpd3Spider(scrapy.Spider):
    name = 'mydpd3'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://sina.com.cn/']

    def parse(self, response):
        pass
