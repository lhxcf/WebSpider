import scrapy


class TbSpider(scrapy.Spider):
    name = "tb"
    allowed_domains = ["taobao.com"]
    start_urls = ["http://taobao.com/"]

    def parse(self, response, *args):
        pass
