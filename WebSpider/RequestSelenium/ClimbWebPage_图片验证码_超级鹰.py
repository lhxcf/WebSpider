# 没有超级鹰账号的要先注册超级鹰账号，初始赠送1000积分，后续 积分要自行购买
# 传统的python自带图像识别库，识别成功率较低，故选择超级鹰平台提供接口调用实现验证码识别验证
# 超级鹰官网 https://www.chaojiying.com/

# 超级鹰接口调用,将下列代码单独存为一个.py文件。放进要调用超级鹰的文件所在文件夹中
'''
import requests
from hashlib import md5


class Chaojiying_Client(object):
    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()
'''

# 文件调用超级鹰核心代码如下
'''
from chaojiying import Chaojiying_Client


def cjy():
    chao = Chaojiying_Client('超级鹰账号', '超级鹰密码', '软件ID')
    im = open('a.png', 'rb').read()   # 打开本地图片文件
    code = chao.PostPic(im, 1902)['pic_str']
    return code  
'''


from WebSpider.chaojiying import Chaojiying_Client
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


# 超级鹰提供了多种验证码识别形式，计算题、英文字符识别、汉字识别，仅需参照超级鹰官网的文档，修改 下方的1902值
# 参考链接：https://www.chaojiying.com/price.html
def cjy():  # 使用超级鹰识别
    chaojiying = Chaojiying_Client('fgwyt123', 'wyt941025', '96001')  # 账号、密码、项目号（这个不用改）
    im = open('a.png', 'rb').read()  # 本地图片文件路径，需要为a.png名字
    code = chaojiying.PostPic(im, 1902)['pic_str']  # 4-6位英文数字用1902
    return code


browser = webdriver.Chrome()
# url = r'E:\验证码反爬\英文图像验证码\index.html'
current_dir = os.path.dirname(os.path.abspath(__file__))  # 获取代码所在的文件夹目录
url = current_dir + '/index.html'  # 获取HTML文件的文件绝对路径，/相当于\\，所以拼接的时候也可以写'\\index.html'
print('此时的文件路径为：' + url)  # 所以如果文件位置固定，可以直接写url = r'文件路径'
browser.get(url)  # 访问网址

# 截取验证码图片
browser.find_element(By.XPATH, '//*[@id="verifyCanvas"]').screenshot('a.png')

# 通过超级鹰识别
result = cjy()
print(result)

# 模拟键盘输入内容，并模拟点击确认按钮
browser.find_element(By.XPATH, '//*[@id="code_input"]').send_keys(result)  # 输入答案
browser.find_element(By.XPATH, '//*[@id="my_button"]').click()  # 模拟点击确认按钮

