from scrapy.spiders import CSVFeedSpider
from myscv.items import MycsvItem


class MycsvspiderSpider(CSVFeedSpider):
    name = 'mycsvspider'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/feed.csv']
    # headers = ['id', 'name', 'description', 'image_link']
    # delimiter = '\t'
    # 定义headers
    headers = ['name', 'sex', 'addr', 'email']
    # 定义间隔符
    delimiter = ','

    # Do any adaptations you need here
    # def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = MycsvItem()
        # 提取各行的name这一列的信息
        i['name'] = row['name'].encode()
        # 提取各行的sex这一列的信息
        i['sex'] = row['sex'].encode()
        # 进行信息输出
        print("名字是：")
        print(i['name'])
        print("性别是：")
        print(i['sex'])
        # 输出完一个记录对应列的信息后，输出一个间隔符，显示起来方便观察
        print("--------------------")
        return i
