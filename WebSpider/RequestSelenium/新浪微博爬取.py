from selenium import webdriver
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/110.0.0.0 Safari/537.36'}

url = 'https://news.sina.com.cn/china/'
browser = webdriver.Chrome()
browser.get(url)
res = browser.page_source
soup = BeautifulSoup(res, 'html.parser')
title = soup.select('.text a')
title_list = []
for i in range(len(title)):
    title_list.append(title[i].get_text())
print(title_list)


