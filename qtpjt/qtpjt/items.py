# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QtpjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 建立picurl存储图片额网址
    picurl = scrapy.Field()
    # 建立picid存储图片网址中的图片名字，以方便构造本地文件名
    picid = scrapy.Field()