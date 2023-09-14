# 三级情感分类
import pandas as pd

df = pd.read_excel('词汇统计结果（在本体中对应）.xlsx')

df = df.groupby(df['情感分类']).sum()
print(df)
# df.to_excel('分组统计结果.xlsx')
