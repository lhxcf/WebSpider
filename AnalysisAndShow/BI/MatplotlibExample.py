import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm


# 对matplotlib进行设置
plt.rcParams['font.sans-serif'] = ['SimHei']    # 设置可显示中文，不出现乱码,字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 设置可显示负号


# 柱状图绘制
'''
plt.figure(figsize=(10, 6))  # 设置画布大小
df = pd.read_excel('情感词汇本体.xlsx')
data = df['词语'].value_counts()

x = data.index[:30]
y = data.values[:30]

plt.title('词汇统计', fontsize=40)   # 设置标题/字体大小
plt.xlabel('词语名称', fontsize=20)     # 设置x轴名称
plt.ylabel('出现次数', fontsize=20)     # 设置y轴名称
plt.tick_params(labelsize=14)  # 设置x，y轴字体大小
plt.xticks(rotation=90)     # x文字轴转90度

for a, b in zip(x, y):
    plt.text(a, b+0.01, b, ha='center', va='bottom', fontsize=7)     # 设置柱状图上方显示具体值,ha:设置水平对齐，va:设置垂直对齐

plt.bar(x, y, color='g')
plt.show()
'''


# 乳腺癌肿瘤半径与平滑度的关系分析图
'''
# 对matplotlib进行设置
plt.rcParams['font.sans-serif'] = ['SimHei']    # 设置可显示中文，不出现乱码,字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 设置可显示负号

df = pd.read_excel('乳腺癌诊断数据集.xlsx')
df = df.sort_values(by='半径')
x = df['半径']
y = df['平滑度']
plt.plot(x, y, color='k')
plt.title('肿瘤半径与平滑度关系', fontsize=30)
plt.xlabel('半径', fontsize=20)
plt.ylabel('平滑度', fontsize=20)
plt.savefig('./img/乳腺癌肿瘤半径与平滑度的关系分析图.png', transparent=False)
plt.show()
'''

# 肿瘤半径频率分布图
'''
df = pd.read_excel('乳腺癌诊断数据集.xlsx')
plt.figure(figsize=(10, 8))
n, bins, patches = plt.hist(df['半径'], bins=100, color='b', alpha=0.5)
plt.xlabel('肿瘤半径', fontsize=20)
plt.ylabel('人数', fontsize=20)
plt.title('肿瘤半径频率分布图')

y = norm.pdf(bins, df['半径'].mean(), df['半径'].std())
ax2 = plt.twinx()
ax2.plot(bins, y, 'k--')
ax2.set_ylabel('概率分布', fontsize=20)
plt.savefig('./img/肿瘤半径频率分布图.png', transparent=False)
plt.show()
'''

# 肿瘤半径与紧凑性的关系(散点图)
'''
df = pd.read_excel('乳腺癌诊断数据集.xlsx')
x = df['半径']
y = df['紧凑性']
plt.scatter(x, y, color='c', marker='p')
plt.legend(labels=['紧凑性'])
plt.title('肿瘤半径与紧凑性的关系', fontsize=40)
plt.xlabel('半径', fontsize=20)
plt.ylabel('紧凑性', fontsize=20)
plt.savefig('./img/肿瘤半径与紧凑性的关系(散点图).png', transparent=False)
plt.show()
'''

