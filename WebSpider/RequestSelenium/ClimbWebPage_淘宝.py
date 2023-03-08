import time
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/110.0.0.0 Safari/537.36'}

# 修改浏览器配置
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome(options=options)

# 用selenium获取cookies
url = 'https://login.taobao.com/member/login.jhtml?spm=a21bo.jianhua.0.0.5' \
      'af911d9aJ8f0A&f=top&redirectURL=http%3A%2F%2Fwww.taobao.com%2F'
browser.get(url)
browser.find_element(By.XPATH, '//*[@id="fm-login-id"]').send_keys('17535691556')
browser.find_element(By.XPATH, '//*[@id="fm-login-password"]').send_keys('479823365c')
browser.find_element(By.XPATH, '//*[@id="login-form"]/div[4]/button').click()
time.sleep(10)
cookies = browser.get_cookies()

# 修改cookies数据格式
cookies_dict = {}
for item in cookies:
    cookies_dict[item['name']] = item['value']

# 利用requests库使用cookies爬取网页
'''
while True:
    try:
        page_no = int(input('请输入要爬取的页数：'))
        break
    except ValueError:
        print('请重新输入要爬取的页数，要为整数！')
goods_name = input('请输入要爬取的商品名称：')
'''
page_no = 100
goods_name = '连衣裙'
try:
    df = pandas.read_excel(fr'~\Desktop\淘宝网{goods_name}商品信息.xlsx')
except FileNotFoundError:
    df = pandas.DataFrame()
    df.to_excel(fr'~\Desktop\淘宝网{goods_name}商品信息.xlsx', index=False)
for i in range(page_no):
    x = 0
    url = f'https://s.taobao.com/search?q={goods_name}&s={x}'
    x += 44
    res = requests.get(url, headers=headers, cookies=cookies_dict).text

    # 模拟通过滑块验证码验证
    if '霸下通用 web 页面-验证码' in res:
        sliders = browser.find_element(By.XPATH, '//*[@id="nc_1_n1z"]')
        action = webdriver.ActionChains(browser)
        action.click_and_hold(sliders).perform()
        time.sleep(2)
        action.move_by_offset(258, 0)
        action.release().perform()

    print(res)
    # 正则表达式提取数据
    title = re.findall('"raw_title":"(.*?)"', res)
    price = re.findall('"view_price":"(.*?)"', res)
    sales = re.findall('"view_sales":"(.*?)人付款"', res)

    #
    df_new = pandas.DataFrame({'商品名称': title, '价格': price, '销量': sales})
    df = pandas.concat([df, df_new], ignore_index=True)
# 将获取的数据存入Excel
    df.to_excel(fr'~\Desktop\淘宝网{goods_name}商品信息.xlsx', index=False)




