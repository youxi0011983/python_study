# middlewares 下载中间件
# 导入随机数模块，目的是随机挑选一个IP池中的IP
import random
# 从setting文件中导入设置好的IPPOOL
from myippool.settings import IPPOOL
# 导入官方文档中的 HttpProoxyMiddleware 对应的模块
from scrapy.contracts.Downloadermiddleware.httpproxy import HttpProxyMiddleware
from scrapy.contracts.default import ReturnsContract

class IPPOOL(HttpProxyMiddleware):
    # 初始化方法
    def __init__(self,ip = ''):
        self.ip = ip

    # process_request()方法，主要进行请求处理
    def process_request(self,request,spider):
        # 先随机选择一个IP
        thisip=random.choice(IPPOOL)
        # 输出当前选择的IP，便于调试观察
        print("当前使用IP是："+thisip["ipaddr"])
        # 将对应的IP实际添加为具体的代理，用该IP进行爬取
        request.meta['proxy'] = "http://"+thisip['ipaddr']