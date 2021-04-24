import pandas as pd

import matplotlib
from matplotlib import pyplot as plt

# 파일은 삭제예정 추후 로딩시 새로운 파일 입력


df = pd.read_csv('src/data/df1.csv')

# 빈공간을 130으로 채운다
# df.fillna(130, inplace = True)

x = df["age"].mean()

df.fillna(x, inplace = True)

new_df = df.dropna()

df.plot()
plt.show()

print(df.to_string())

print(new_df.to_string())