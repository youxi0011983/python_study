# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter


class MysqlpjtPipeline:
    def __init__(self):
        # 刚开始时链接对应数据库
        self.conn = pymysql.connect(host="xiongliang.synology.me", passwd="", user="root",
                                    db='mypydb')

    def process_item(self, item, spider):
        # 将获取得到的name、url、hits、comment分别赋值给变量
        name = item["name"][0]
        key = item["keywd"][0]
        # 构造对用的sql语句
        sql = "insert into mytb(title, keywd) values('" + name + "','" + key + "')"
        # 通过query 实现执行对应的sql语句
        self.conn.cursor().execute(sql)
        return item

    def close_spider(self, spider):
        self.conn.close()
