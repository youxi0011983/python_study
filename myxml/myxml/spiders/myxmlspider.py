# -*- coding utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem


class MyxmlspiderSpider(XMLFeedSpider):
    name = 'myxmlspider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/rss/1361074815.xml']
    # iterator 属性设置的是使用那个迭代器，默认值"iternodes"
    iterator = 'iternodes' # you can change this; see the docs
    # itertag 属性主要用来设置开始迭代的节点。
    itertag = 'item' # change it accordingly

    # 在节点与所提供的标签名相符合的时候会被调用
    def parse_node(self, response, selector):
        item = MyxmlItem()
        # 利用xpath表达式将对应的信息提取出来，并存储到对应的item中
        item['title'] = node.xpath("/rss/channel/item/title/text()").extract()
        item['link'] = node.xpath("/rss/channel/item/link/text()").extract()
        item['author'] = node.xpath("/rss/channel/item/author/text()").extract()
        # 通过for循环以此表里出提取出来存在item中的信息并输出
        for j in range(len(item['title'])):
            print("第"+str(j+1)+"篇文章")
            print("标题时：")
            print(item['title'][j])
            print("对应的链接是：")
            print(item['link'][j])
            print("对应的作者是：")
            print(item['author'][j])
            print("--------------------------------")
        return item
