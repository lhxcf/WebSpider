import requests
import json
import re

news_type = 'new'       # 爬取种类：hot/new
target = 500       # 爬取条数

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
           'Accept': 'application/json, text/javascript, */*; q=0.01',
           'Cookie': 'bid=Il1wefKI7VI; douban-fav-remind=1; __gads=ID=54c99611d5f21385-222b5665f5d800f6:T=1671602837:'
                     'RT=1671602837:S=ALNI_Ma1mA4Tw76dzc1k7garZk2RwBLsqw; __utmz=30149280.1671602840.1.1.utmcsr=baidu|'
                     'utmccn=(organic)|utmcmd=organic; __gpi=UID=00000b9506553b5d:T=1671602837:RT=1681367891:S=ALNI_M'
                     'ZtLr8n5njTpa_eU6PEpQsmqEwgwg; ap_v=0,6.0; __utma=30149280.1088756327.1671602840.1681367803.1681'
                     '780545.4; __utmc=30149280; __utmt=1; __utmb=30149280.1.10.1681780545',
           'Host': 'm.douban.com',
           'Referer': 'https://www.douban.com/gallery/topic/148466/?sort=hot'}


views_hot = []
count = 0
for i in range(0, target+1000, 20):
    url = f'https://m.douban.com/rexxar/api/v2/gallery/topic/148466/items?from_web=1&sort={news_type}&start={i}&' \
          f'count=20&status_full_text=1&guest_only=0&ck=null'
    res = requests.get(url, headers=headers)
    data = json.loads(res.text)['items']
    for item in data:
        try:
            strs = item['target']['status']['text']
        except KeyError:
            strs = item['abstract']
        strs = re.sub(r'[\n\r]', '', strs)
        views_hot.append(strs)
        count += 1
        print(f"已爬取{count}条")
    if count >= target:
        break


# 将爬取的评论存为文本文档
with open(f'{news_type}评论.txt', 'w', encoding="utf-8") as f:
    for i in views_hot:
        f.write(i+'\n')
# 格式化输出json
# data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))
# print(data)
