# 在下载器中间件（middlewares.py)中找到ScrapyexampleDownloaderMiddleware下的process_request()方法，写下ip代理代码，当一个IP地址无效时，Scrapy
# 会自动切换IP
# 还要在settings.py文件中将ROBOTSTXT_OBEY值改为False,将DOWNLOADED_MIDDLEWARES激活

import scrapy
import requests
import json
import time
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
           'Chrome/110.0.0.0 Safari/537.36'}


class IpSpider(scrapy.Spider):
    name = "ip"
    allowed_domains = ["baidu.com"]
    start_urls = ["https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8992368402812241632&ipn=rj&"
                  "ct=201326592&is=&fp=result&fr=&word=%E5%A3%81%E7%BA%B8&cg=wallpaper&queryWord=%E5%A3%81%E7%BA%B8&"
                  "cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&"
                  "face=&istype=&qc=&nc=1&expermode=&nojc=&isAsync=&pn=0&rn=30&gsm=1e&1677835733571="]
    for i in range(1, 100):
        start_urls.append(f"https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8992368402812241632&ipn=rj&"
                          f"ct=201326592&is=&fp=result&fr=&word=%E5%A3%81%E7%BA%B8&cg=wallpaper&queryWord="
                          f"%E5%A3%81%E7%BA%B8&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&"
                          f"s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&expermode=&nojc=&isAsync=&pn={i}&rn=30&"
                          f"gsm=1e&1677835733571=")

    def parse(self, response, *args, **kwargs):
        data = response.text
        js = json.loads(data)
        count = 0
        for i in js['data']:
            try:
                title = i['fromPageTitle']
                img_url = i['thumbURL']
                count += 1
            except KeyError:
                continue

            # 图片的title可能相同，因此引入时间变量，避免因图片名重复而让后来的同名图片覆写在前一图片文件中
            # 图片名中不能包含冒号
            path = fr"C:\Users\32858\Desktop\images\{title}{time.strftime('%H%M%S', time.gmtime(time.time()))}"+".png"
            res = requests.get(img_url, headers=headers)

            f = open(path, 'wb')  # 注意以二进制形式打开
            f.write(res.content)    # 注意以二进制形式存入
            f.close()
            print(f'{count}页下载完毕: {title}')

