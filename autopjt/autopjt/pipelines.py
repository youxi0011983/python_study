# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import codecs
import json


class AutopjtPipeline:
    def __init__(self):
        # 打开mydata。json文件
        self.file = codecs.open("d:/code/autopjt/mydata.json", "wb", encoding="utf-8")

    def process_item(self, item, spider):
        i = json.dumps(dict(item),ensure_ascii=False)
        # 每条数据后加上踢换行
        line = i +'\n'
        # 数据写入到 mydata.json文件中
        self.file.write(line)
        return item

    def close_spider(self,spider):
        # 关闭 mydata.json文件
        self.file.close()