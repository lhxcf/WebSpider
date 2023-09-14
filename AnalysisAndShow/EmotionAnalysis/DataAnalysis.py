import pandas as pd

# 情感词汇库路径
pathTxt = '情感词汇本体.xlsx'

# 读取情感词汇库
df = pd.read_excel(pathTxt)

# 情感分析文件路径
pathTxt = r"hot评论.txt"

with open(pathTxt, "r", encoding='utf-8') as f:
    texts = f.readlines()

i = 0
df.index = df['词语']
df_res = pd.DataFrame({'评论': 'text', '出现词语统计': ' '}, index=[i])
for text in texts:
    words = {}
    for word in df.index:
        try:
            num = text.count(word)
            if num > 0:
                words[word] = num
        except TypeError:
            continue
    print('完成一条')
    data = []
    for key, val in words.items():
        data.append(f'{key}: {val}')
    df_res1 = pd.DataFrame({'评论': text, '出现词语统计': ',  '.join(data)}, index=[i])
    df_res = pd.concat([df_res, df_res1], ignore_index=True)
    i += 1

# 排除不出现项
# df_res[df_res['计数'] != 0].to_excel('词汇统计结果.xlsx', index=False)

# 输出所有值
df_res.to_excel('词汇统计结果.xlsx', index=False)


# 排除的词汇


# 统计高频词
# for word in words:
#     if len(word) == 1:    # 忽略单个词语
#         continue
#     else:
#         counts[word] = counts.get(word, 0) + 1
# flag = 0
# for key, val in counts.items():
#     if val >= 50 and key not in exclude:
#         print(f"{key}:{val}      ", end="")
#         flag += 1
#         if flag % 5 == 0:
#             print('\n')


