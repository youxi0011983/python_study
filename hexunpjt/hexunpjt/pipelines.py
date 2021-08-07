# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class HexunpjtPipeline:
    def __init__(self):
        # 刚开始时链接对应数据库
        self.conn = pymysql.connect(host="xiongliang.synology.me", passwd="q1w2e3r4", user="root",
                                    db='hexun')

    def process_item(self, item, spider):
        for j in range(0, len(item["name"])):
            # 将获取得到的name、url、hits、comment分别赋值给变量
            name = item["name"][j]
            url = item["url"][j]
            hits = item["hits"][j]
            comment = item["comment"][j]
            # 构造对用的sql语句,实现将获取到的对应数据插入数据库中
            sql = "insert into myhexun(name, url,htis,comment) values('" + name + "','" + url + "','" + hits + "','" + comment + "')"
            # 通过query 实现执行对应的sql语句
            self.conn.cursor().execute(sql)
        return item

    def close_spider(self, spider):
        self.conn.close()
