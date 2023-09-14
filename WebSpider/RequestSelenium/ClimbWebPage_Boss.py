# 爬取boss直聘页面
# 多线程
# 智能IP切换
import numpy as np
import time
import re
import queue
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import threading
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/112.0.0.0 Safari/537.36'}
page_number = 10    # 要获取的页数
post_name = 'python'    # 职位名称
city_code = '101230100'    # 城市代码，需自行进入网站地址栏查看填写，否则不要改动
url_queue = queue.Queue()
for x in range(page_number):
    url_x = f'https://www.zhipin.com/web/geek/job?query={post_name}&city={city_code}&page={x+1}'
    url_queue.put(url_x)

# ip代理放入队列,代理要自己去买
ip_queue = queue.Queue()
df = pd.read_excel('Ip代理.xlsx')
for ip in df['ip']:
    ip_queue.put(ip)


# ip代理，切换ip
def change_ip():
    proxy = str(ip_queue.get())
    proxy.strip()
    print(f'IP切换为：{proxy}')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=' + proxy)
    driver = webdriver.Chrome(options=chrome_options)


# 爬取函数
# 返回二维表格，即pandas.DataFrame数据类型
# 爬取后进行数据清洗，并存为Excel
def crawl():
    driver = webdriver.Chrome()
    df_res = pd.DataFrame()   # 最终结果
    while not url_queue.empty():
        try:
            driver.get(url_queue.get())
            time.sleep(5)
            res = driver.page_source

            # 模拟完成安全验证
            while '点击进行验证' in res:
                driver.find_element(By.XPATH, '//*[@id="wrap"]/div/div[1]/div/button').click()

            # 当出现403页面时切换Ip
            while '403' in res:
                proxy = ip_queue.get()
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--proxy-server' + proxy)
                driver = webdriver.Chrome(options=chrome_options)
                driver.get(url_queue.get())
                time.sleep(5)
                print(f'ip切换为:{proxy}')
                res = driver.page_source

            # 用正则表达式获取html中相关信息
            job_name_re = '<span class="job-name">(.*?)</span>'
            job_area_re = '<span class="job-area">(.*?)</span>'
            request_re = '<span class="job-area">.*?</span><ul class="tag-list">(.*?)</ul>'
            job_name = re.findall(job_name_re, res)
            job_area = re.findall(job_area_re, res)
            request = re.findall(request_re, res, re.S)

            # 数据清洗
            for i in range(len(request)):
                request[i] = re.sub('<.*?>', ' ', request[i]).lstrip()
                request[i] = re.sub(r'\s{4}', '/', request[i])
            job_name = np.array(job_name)
            job_area = np.array(job_area)
            request = np.array(request)

            # 利用pandas将获取到的信息到处为Excel
            df_p = pd.DataFrame({'工作名称': job_name, '工作地点': job_area, '工作要求': request})
            df_res = pd.concat([df_res, df_p], ignore_index=True)
        except ValueError:
            print('爬取失败！')
            continue
    driver.quit()
    df_res.to_excel('Boss直聘.xlsx', index=False)


# 多线程爬取
if __name__ == '__main__':
    start_time = time.time()
    thread_list = []
    for t in range(1):
        thread_list.append(threading.Thread(target=crawl))
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
    end_time = time.time()
    print(f'\n爬取共用时：{round(end_time - start_time, 2)}秒')


