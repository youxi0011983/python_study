import scrapy


class Mydpd2Spider(scrapy.Spider):
    name = 'mydpd2'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://sina.com.cn/']

    def parse(self, response):
        pass
