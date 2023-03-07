import requests
import json
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
           'Chrome/110.0.0.0 Safari/537.36'}
start_urls = ["https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8992368402812241632&ipn=rj&"
              "ct=201326592&is=&fp=result&fr=&word=%E5%A3%81%E7%BA%B8&cg=wallpaper&queryWord=%E5%A3%81%E7%BA%B8&"
              "cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&"
              "face=&istype=&qc=&nc=1&expermode=&nojc=&isAsync=&pn=0&rn=30&gsm=1e&1677835733571="]
data = requests.get(start_urls[0], headers=headers).text
js = json.loads(data)
count = 0
for i in js['data']:
    try:
        title = i['fromPageTitle']
        img_url = i['thumbURL']
        count += 1
    except KeyError:
        continue
    path = fr'C:\Users\32858\Desktop\images\{title}.png'
    res = requests.get(img_url, headers=headers)

    with open(path, 'wb') as f:
        f.write(res.content)
        print(f'{title} 下载完毕')
print(f'共{count}张图片下载完毕')