import pandas as pd

df = pd.read_excel('all_sales.xlsx')

# 读所有行的spu以及level1列的值，这里需要嵌套列表
df_delete_column = df.drop(labels='spu', axis=1)

df_delete_column.to_excel('new.xlsx')
