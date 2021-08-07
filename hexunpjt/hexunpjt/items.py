# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HexunpjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 建立name存储文章名
    name = scrapy.Field()
    # 建立url存储文章地址
    url= scrapy.Field()
    # 建立hits存储文章阅读数
    hits = scrapy.Field()
    # 建立comment存储文章评论数
    comment = scrapy.Field()
