from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('mysql+pymysql://root:000000@localhost:3306/publicopinionanalysis')
df = pd.read_excel(r'~\Desktop\淘宝网连衣裙商品信息.xlsx')

# 利用函数去重，删除表格中重复项，避免数据库中主键重复
df = df.drop_duplicates()
print(len(df))
# 其中的engine代表数据库连接，pandas中的engine只能是sqlalchemy中的数据库连接
df.to_sql('goods', engine, index=False, if_exists='append')


