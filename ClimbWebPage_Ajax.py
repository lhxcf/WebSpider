# 爬取采用Ajax技术的网页，核心在于获取请求头自带的接口及其页面切换规律。
# 打开开发者工具，单击Network选项卡，选择XHR选项后刷新页面，往下翻网页，查看左侧最新显示的文件
# 其中Request Headers中的X-Requested-With的值显示为：XMLHttpRequest，则表示此网页采用Ajax技术
# 接口网址为General下的Request URL对应值
# 观看视频时，在开发者工具中的Consle选项卡中输入代码：“document.querySelector('video')playbackRate = 3.0”。其中3.0代表用3倍速播放

# 使用selenium滑动网页代码如下
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.oschina.net/blog')
browser.maximize_window()  # 将模拟浏览器窗口最大化
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # 引号内内容未js代码，.execute_script函数模拟执行js代码
