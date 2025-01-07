
import re
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import random
import requests


n = 17  # 题目数量
y = 200  # 要填写的份数
duo = [5, 7, 8, 15, 17]  # 多选题序号(不选选项的最后一项)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/110.0.0.0 Safari/537.36'}

url = 'https://www.wjx.cn/vm/PpFsdWc.aspx'
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome(options=options)
browser.maximize_window()


for i_ in range(y):
    # mainWindow = browser.current_window_handle
    # browser.execute_script("window.open('','_blank');")
    # handel = browser.window_handles
    # browser.switch_to.window(handel[1])
    browser.get(url)
    res = browser.page_source
    for i in range(1, n+1):
        select = re.findall(rf'div class="label"[^>]*for="q{i}_(.*?)"', res)
        if i in duo:
            len_ = len(select) - 2
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
    # time.sleep(0.3)
    time.sleep(0.5)
    try:
        # browser.find_element(By.CLASS_NAME, 'rect-bottom').click()
        browser.find_element(By.CLASS_NAME, 'layui-layer-btn0').click()
    except:
        pass
    try:
        browser.find_element(By.CLASS_NAME, 'sm-ico-wave').click()
        time.sleep(3)
    except:
        pass
    try:
        action = webdriver.ActionChains(browser)
        button = browser.find_element(By.ID, 'nc_1_n1z')
        action.drag_and_drop_by_offset(button, 338, 0).perform()
    except:
        pass
    # browser.close()
    # browser.switch_to.window(mainWindow)
    time.sleep(3)



