# 调用selenium库进行爬取
# 在下载器中间件中编写代码，包括初始化方法和在process_request中编写代码
import scrapy


class TbSpider(scrapy.Spider):
    name = "tb"
    allowed_domains = ["taobao.com"]
    start_urls = ["https://s.taobao.com/search?q=连衣裙"]

    def parse(self, response, *args):

        pass
