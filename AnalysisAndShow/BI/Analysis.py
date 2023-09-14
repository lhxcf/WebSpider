import pandas as pd
import numpy as np

df_path = '乳腺癌诊断数据集.xlsx'
df = pd.read_excel(df_path)

bj = df['半径']

print(bj.max(), bj.min())
