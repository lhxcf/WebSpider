
import re
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import random
import requests
import urllib.request


n = 20  # 题目数量
y = 65  # 要填写的份数
duo = [-1]  # 多选题序号

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/110.0.0.0 Safari/537.36'}

url = 'https://mp.weixin.qq.com/s/kJAg5VjoFOi1PSpR8gtJtw'

res = requests.get(url).text

title = re.findall('<a href="(.*?)" target="_blank" data-linktype="2">', res)
title.insert(17, 'http://mp.weixin.qq.com/s?__biz=MzI5MzYzNDU5Mg==&amp;mid=2247514610&amp;idx=6&amp;sn=630cae29c59631a353ebc46adea64b53&amp;chksm=ec6deebddb1a67abb014e3526ff5b458f0985b8d66df47c329cf892168f44233e15c8f57d19b&amp;scene=21#wechat_redirect')
title.append('http://mp.weixin.qq.com/s?__biz=MzI5MzYzNDU5Mg==&amp;mid=2247504030&amp;idx=2&amp;sn=e0f9060b6ed569f9ba80735c2a31ca28&amp;chksm=ec6d87d1db1a0ec7d358dcc635d58d15ef2e7959342d5ec67cb8444940d1320ed17ff3abc6ec&amp;scene=21#wechat_redirect')
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome()
browser.maximize_window()

browser.get(title[0])
time.sleep(30)
print(browser.page_source)
browser.find_elements(By.CLASS_NAME, 'pic_mid_play')[0].click()
browser.find_elements(By.CLASS_NAME, 'pic_mid_play')[2].click()
res = browser.page_source
urls = re.findall('<video .*? src="(.*?)"', res)

count = 1
urllib.request.urlretrieve(urls[0], fr'C:\Users\32858\Desktop\针灸视频\第{count}集.mp4')
'''

for i_ in range(y):
    # mainWindow = browser.current_window_handle
    # browser.execute_script("window.open('','_blank');")
    # handel = browser.window_handles
    # browser.switch_to.window(handel[1])
    browser.get(url)
    res = browser.page_source
    for i in range(1, n+1):
        select = re.findall(rf'div class="label" for="q{i}_(.*?)"', res)
        if i in duo:
            len_ = len(select) - 1
        else:
            len_ = len(select)
        try:
            x = random.randint(1, len_)
        except:
            pass
        try:
            browser.find_element(By.XPATH, f'//*[@id="div{i}"]/div[2]/div[{x}]/div').click()
        except:
            pass
        # browser.find_element(By.XPATH, f'//*[@id="div{i}"]/div[2]/div[{x}]/div').click()
    print(i_)
    browser.find_element(By.XPATH, f'//*[@id="ctlNext"]').click()
    time.sleep(0.3)
    try:
        browser.find_element(By.CLASS_NAME, 'layui-layer-btn0').click()
        browser.find_element(By.CLASS_NAME, 'sm-ico-wave').click()
        time.sleep(3)

        action = webdriver.ActionChains(browser)
        button = browser.find_element(By.ID, 'nc_1_n1z')
        action.drag_and_drop_by_offset(button, 338, 0).perform()

    except:
        pass
    # browser.close()
    # browser.switch_to.window(mainWindow)
    time.sleep(3)

'''

