# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
   urlname = scrapy.Field()
   urlkey = scrapy.Field()
   urlcr = scrapy.Field()
   urladdr = scrapy.Field()
