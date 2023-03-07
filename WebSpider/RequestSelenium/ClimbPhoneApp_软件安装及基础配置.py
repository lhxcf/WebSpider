#     下载相关软件：    pc端对应：
#              夜神模拟器  ->  谷歌浏览器    (https://www.yeshen.com)
#               Node.js  ->  安装软件所用的插件    (https://nodejs.org/zh-cn/download/)   验证是否安装成功：cmd中输入 “node -v”
#                   JDK  ->  安装软件所用的插件    (https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html)
#        Android Studio  ->  安装软件所用的插件    (https://www.androiddevtools.cn/)
#                Appium  ->  Selenium库中用到的模拟浏览器ChromeDriver    (http://appium.io/)
# Appium-Python-Client库  ->  Selenium库
# 安装JDK主要是为了方便之后安装Android Studio和Appium，两者都需要Java环境
# Android Studio安装：进入网站后，Android SDK工具 -> SDK Tools
# 安装后启动安装文件夹内的SDK Manager.exe,勾选安装Tools的前三个、Extras中的Android Support Repository 和 Google USB Driver
# 在cmd命令窗口运行指令：connect 127.0.0.1:62001,使用adb devices 检验是否连接成功
# 用adb(Android系统调试桥)查看App信息：（1）adb shell    （2）dumpsys activity | grep mFocusedActivity

from appium import webdriver
from appium.webdriver.common.appiumby import By

# 获得包名和活动名，要先进入相应的app
desired_caps = {
    'newCommandTimeout': 3600,  # 3600秒无操作自动退出Appium
    'platformName': 'Android',  # Android平台
    'deviceName': '127.0.0.1:62001',  # 模拟器设备，默认端口62001
    'platformVersion': '7.1.2',  # 平台版本号
    'udid': '127.0.0.1:62001',  # 设备id，和设备名相同
    'appPackage': 'com.tencent.mm',  # 包名
    'appActivity': '.plugin.account.ui.LoginPasswordUI'  # 活动名
}

# 连接手机前要先打开手机的开发者模式
# 连接手机，并打开微信App
browser = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
data = browser.page_source
print(data)


# 获取屏幕尺寸
window_size = browser.get_window_size()

# 屏幕截图,括号内为存储路径及图片名
browser.save_screenshot('图片名.png')

# 获取屏幕中显示的内容的源代码
res = browser.page_source

# 模拟滑动屏幕
browser.swipe(50, 1000, 50, 200)  # 屏幕内容向上滑动
browser.swipe(50, 200, 50, 1000)  # 屏幕内容向下滑动

# 模拟点击屏幕
browser.tap([(450, 800), (250, 800)])

# UI Automator Viewer
# 4个重要的属性：
#   （1）bounds：位置，左上角和左下角的坐标
#   （2）name: 对应text值
#   （3）id: 对应resource-id
#   （4）class: 类似html中的class属性

# 定位单个元素
browser.find_element(By.ID, 'id值')
browser.find_element(By.NAME, 'name值')

# 定位多个元素,并获取对应文本
data = browser.find_elements(By.ID, 'id值')
for i in data:
    print(i.text)
browser.find_elements(By.NAME, 'name值')










