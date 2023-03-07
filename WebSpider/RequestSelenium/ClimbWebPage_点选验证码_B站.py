from selenium import webdriver
from RequestSelenium.chaojiying import Chaojiying_Client
from selenium.webdriver.common.by import By
import time
# 超级鹰账号要更换，换位自己的账号
# 访问网址
browser = webdriver.Chrome()
url = 'https://passport.bilibili.com/login'
browser.get(url)

# 输入账号密码，并点击登录按钮
user = '18810623690'
password = 'lzhqwer4321'
browser.find_element(By.ID, 'login-username').send_keys(user)  # 输入账号
browser.find_element(By.ID, 'login-passwd').send_keys(password)  # 输入密码
browser.find_element(By.XPATH, '//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()  # 点击登录按钮

time.sleep(2)


def yzm():  # 定义验证码识别函数
    # 获取点选验证码的图片
    canvas = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]')
    canvas.screenshot('bilibili.png')

    # 使用超级鹰识别
    chaojiying = Chaojiying_Client('fgwyt123', 'wyt941025', '905908')  # 用户中心>>软件ID 生成一个替换
    im = open('bilibili.png', 'rb').read()  # 本地图片文件路径
    res = chaojiying.PostPic(im, 9004)['pic_str']
    print(f'res = {res}')

    # 对获取的坐标数据进行一些处理
    all_location = []  # 下面开始规范各点坐标
    list_temp = res.split('|')  # 利用“|”将各个点的坐标提取出来，list_temp是个临时列表
    print(list_temp)

    for i in list_temp:  # 遍历上面的临时列表
        list_i = []  # 用来存储每点的坐标
        x = int(i.split(',')[0])  # 第一个元素为横坐标，并将字符串转为整数
        y = int(i.split(',')[1])  # 第二个元素为纵坐标，并将字符串转为整数
        list_i.append(x)  # 添加横坐标
        list_i.append(y)  # 添加纵坐标
        all_location.append(list_i)  # 汇总每一点的坐标
    print(all_location)  # 此时转换成立规范的坐标

    # 依次模拟点击文字
    for i in all_location:
        x = i[0]
        y = i[1]
        action = webdriver.ActionChains(browser)  # 启动Selenium的动作链
        action.move_to_element_with_offset(canvas, x, y).click().perform()  # 根据坐标点击
        time.sleep(1)

    # 点击确定按钮，登录成功
    time.sleep(3)
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[6]/div/div/div[3]/a/div').click()  # 点击确定按钮

    # 等待2秒后，获取此时的网页源代码
    time.sleep(2)
    data = browser.page_source
    return data


# 无限尝试验证码，直到识别正确为止
while True:
    result = yzm()  # 调取上面定义的yzm()函数
    if '密码登录' in result and '短信登录' in result:  # 判断是否还是首页，如果是，休息3秒后继续循环
        time.sleep(3)  # 休息3秒后，继续执行循环
    else:  # 判断是否还是首页，如果不是，退出循环
        break  # 如果登录成功，则break退出循环

