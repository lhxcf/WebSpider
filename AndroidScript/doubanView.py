import selenium.webdriver.common.by
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def drop_down():
    for x in range(1, 100, 2):
        time.sleep(1)
        j = x/9
        # javascript:前段脚本语言 操作浏览器 页面 动态效果
        js='document.documentElement.scrollTop=document.documentElement.scrollHeight*%f' % j
        driver.execute_script(js)


driver = webdriver.Chrome()
driver.get('https://www.douban.com/gallery/topic/148466/?sort=hot')
drop_down()
items = driver.find_elements(By.XPATH, '//*[@id="topic-items"]/div/div')
text_list = []
for item in items:
    try:
        text_list.append(item.find_element(By.CSS_SELECTOR, '.status-preview').text)
    except:
        text_list.append("null")

with open('评论3.txt', 'w', encoding="utf-8") as f:
    for i in text_list:
        f.write(i+'\n')