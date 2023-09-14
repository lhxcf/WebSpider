import pandas as pd

# 情感词汇库路径
pathTxt = r'情感词汇本体.xlsx'

# 读取情感词汇库
df = pd.read_excel(pathTxt)

# 情感分析文件路径
pathTxt = r".txt"

with open(pathTxt, "r", encoding='utf-8') as f:
    texts = f.readlines()

df.index = df['词语']
words = {}
for word in df.index:
    words[word] = 0
i = 1
for word in df.index:
    for text in texts:
        try:
            words[word] += text.count(word)
        except:
            continue
    print(f"完成{i}词")
    i += 1

df_res = pd.DataFrame({'词语': words.keys(), '计数': words.values()})


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


