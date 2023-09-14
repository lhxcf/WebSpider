from bs4 import BeautifulSoup
import requests
import requests
import threading    # 导入多线程库
import time
import queue
import multiprocessing  # 导入多进程库
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/110.0.0.0 Safari/537.36'}


def crawl(company):    # 注意元组传参是用*company,字典传参使用**company
    url = 'https://cn.bing.com/search?q=' + company
    res = requests.get(url, headers=headers, timeout=10).text
    print(res)


if __name__ == '__main__':
    start_time = time.time()

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    companies = ['阿里巴巴', '腾讯', '网易']
    pool.map(crawl, companies)

    end_time = time.time()
    total_time = end_time - start_time
    print('\n\n爬虫共计用时' + ' ' + str(round(total_time, 2)) + ' ' + '秒')


