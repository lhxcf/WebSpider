# 爬取boss直聘页面
import time

import pandas
import requests
import threading
import queue
import pandas as pd
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/110.0.0.0 Safari/537.36'}
url_queue = queue.Queue()
url_queue.put('http://www.66ip.cn/index.html')
for i in range(2, 2999):
    url_i = f'http://www.66ip.cn/{i}.html'
    url_queue.put(url_i)


# 爬取函数
def crawl():
    try:
        df = pd.read_excel('66免费代理网Ip代理.xlsx')
    except FileNotFoundError:
        df = pandas.DataFrame()
    x = 1
    while not url_queue.empty():
        try:
            print(f'正在爬取第{x}页...')
            x += 1
            url = url_queue.get()
            res = requests.get(url)
            res.encoding = 'gb2312'
            table = pd.read_html(res.text)[1]
            df_res = pd.DataFrame(table)
            df_res.columns = df_res.values.tolist()[0]
            df_res.drop([0], inplace=True)
            for y in range(1, len(df_res)):
                if df_res['ip'][y] in df:
                    df_res.drop(index=df_res['ip'][y].index, axis=0, inplace=True)
            df = pd.concat([df, df_res], ignore_index=True)
            # time.sleep(3)
        except:
            print('一页爬取失败！')
            continue
    df.to_excel('66免费代理网Ip代理.xlsx', index=False)
    print('一页爬取成功！')


if __name__ == '__main__':
    start_time = time.time()
    thread_list = []
    for i in range(10):
        thread_list.append(threading.Thread(target=crawl))
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
    end_time = time.time()
    print(f'\n爬取共用时：{round(end_time - start_time, 2)}秒')
