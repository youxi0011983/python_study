# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import urllib.request

from itemadapter import ItemAdapter


class QtpjtPipeline:
    def process_item(self, item, spider):
        # 一个图片列表页面中有多张图片，通过for循环依次将图片存储到本地
        for i in range(0, len(item["picurl"])):
            thispic = item["picurl"][i]
            # 根据上面总结的规律构造出原图片的URL地址：:
            trueurl = thispic + "_1024.jpg"
            # 构造出图片在本地存储的地址
            localpath = "d:/code/qtpjt/pic/" + item['picid'][i] + ".jpg"
            # 通过urlLib.request.urlretieve()将图片下载到本地
            urllib.request.urlretrieve(trueurl, filename=localpath)
        return item
