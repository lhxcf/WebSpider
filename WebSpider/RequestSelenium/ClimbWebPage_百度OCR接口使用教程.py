from aip import AipOcr  # 得先pip install baidu-aip

# 下面3行内容为自己的APP_ID,API_KEY,SECRET_KEY
APP_ID = '11352343'
API_KEY = 'Nd5Z1NkGoLDvHwBnD2bFLpCE'
SECRET_KEY = 'A9FsnnPj1Ys2Gof70SNgYo23hKOIK8Os'

# 把上面输入的账号信息传入接口
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 自己图片的地址，其他地方就不用改了
filePath = r'诗.jpg'


# 定义打开文件的函数
def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()


# 定义参数变量
options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}

# 调用通用文字识别接口并打印结果
result = aipOcr.basicGeneral(get_file_content(filePath), options)
print(result)

# 打印具体内容
words_result = result['words_result']
for i in range(len(words_result)):
    print(words_result[i]['words'])
