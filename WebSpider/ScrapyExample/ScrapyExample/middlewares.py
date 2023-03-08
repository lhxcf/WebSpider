# 引入相应的库

from selenium import webdriver
import time
from scrapy.http import  HtmlResponse
from selenium.webdriver.common.by import By

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import requests
import time
from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class ScrapyexampleSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class ScrapyexampleDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s
    # 使用selenium库爬取的代码
    # def __int__(self):
    #     self.browser = webdriver.Chrome()

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called

        # ip代理代码块
        # proxy = requests.get('http://webapi.http.zhimacangku.com/getip?num=1&type=3&pro=&city=0&yys=0&port=1&time=1&'
        #                      'ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=').text
        # proxy = proxy.strip()
        # proxies = 'http://' + proxy
        # print('提取ip为：' + proxy)
        # request.meta['proxy'] = proxies
        # time.sleep(4)

        # Cookies模拟登录
        # 修改浏览器配置
        # options = webdriver.ChromeOptions()
        # options.add_argument("--disable-blink-features=AutomationControlled")
        # browser = webdriver.Chrome(options=options)
        #
        # browser.get('https://login.taobao.com/member/login.jhtml?spm=a21bo.jianhua.754894437.1.5af911d9AfQQs6&'
        #             'f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F')
        # browser.find_element(By.XPATH, '//*[@id="fm-login-id"]').send_keys('17535691556')
        # browser.find_element(By.XPATH, '//*[@id="fm-login-password"]').send_keys('479823365c')
        # browser.find_element(By.XPATH, '//*[@id="login-form"]/div[4]/button').click()
        # time.sleep(7)
        # cookies = browser.get_cookies()
        # request.cookies = cookies
        # browser.quit()

        # 使用selenium库爬取的代码
        # self.browser.get(request.url)
        # time.sleep(2)
        # body = self.browser.page_source
        # return HtmlResponse(self.browser.current_url, body=body, encoding='utf-8', request=request)
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
