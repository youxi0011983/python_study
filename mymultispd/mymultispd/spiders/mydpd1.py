import scrapy


class Mydpd1Spider(scrapy.Spider):
    name = 'mydpd1'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://sina.com.cn/']

    def parse(self, response):
        pass
