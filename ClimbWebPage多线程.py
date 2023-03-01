# 多线程爬虫案例
# 通常只新建5-10个线程，然后把多个网址分配给多个线程去爬取，新建太多线程会浪费计算机资源
# 列表是线程不安全的
# 多线程尽量不要工用数据/global，当然可以用线程锁，
import requests
import threading    # 导入多线程库
import time
import queue
from bs4 import BeautifulSoup
companies = ['阿里巴巴', '腾讯', '网易']
url_queue = queue.Queue()
for company in companies:
    url_i = 'https://cn.bing.com/search?q=' + company
    url_queue.put(url_i)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/110.0.0.0 Safari/537.36'}


# 默认爬取‘阿里巴巴’界面
def crawl():    # 注意元祖传参是用*company,字典传参使用**company
    while not url_queue.empty():
        url = url_queue.get()   # 提取队列里的元素，先进先出
        try:
            res = requests.get(url, headers=headers, timeout=10).text
            soup = BeautifulSoup(res, 'html.parser').prettify()     # 美化爬取的html
            print(soup)
        except:
            res = '访问超时'


start_time = time.time()
thread_list = []
for i in range(7):
    t = threading.Thread(target=crawl)  # 若companies仅有一个参数，则参数后必须加’,‘， 例如args=('网易',)
    thread_list.append(t)

for t in thread_list:   # 启动线程
    t.start()
for t in thread_list:   # 加入线程，两个循环不能合并，否则线程无效
    t.join()

end_time = time.time()
total_time = end_time - start_time
print('\n\n爬虫共计用时' + ' ' + str(round(total_time, 2)) + ' ' + '秒')

'''
#此代码块中，多线程无效，5个线程分别执行一次text((1,))
from bs4 import BeautifulSoup
import requests
import requests
import threading    # 导入多线程库
import time
import queue
import multiprocessing  # 导入多进程库
from bs4 import BeautifulSoup


def text2(*x):
    sum_ = 0
    y = 0
    global lock
    lock.acquire()
    for x_ in x:
        for x1 in range(x_):
            sum_ += 1
            time.sleep(3)
        print(f'第{y+1}个结果为{sum_}')
    print('任务二结束' + str(sum_))
    lock.release()


start_time = time.time()
thread_list = []
lock = threading.Lock()
for i in range(5):
    t = threading.Thread(target=text2, args=(1, ))  # 若companies仅有一个参数，则参数后必须加’,‘， 例如args=('网易',)
    thread_list.append(t)
for t in thread_list:   # 启动线程
    t.start()
for t in thread_list:   # 加入线程，两个循环不能合并，否则线程无效
    t.join()
end_time = time.time()
total_time = end_time - start_time
print('\n\n爬虫共计用时' + ' ' + str(round(total_time, 2)) + ' ' + '秒')
'''