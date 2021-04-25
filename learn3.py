# 유튜브를 보고 배워보는 파이썬 데이터 분석

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from scipy import sparse

# 데이터를 열어서 df 보기
iris = datasets.load_iris()
# print(iris.DESCR)
iris.keys()
# iris.data
# iris.target

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['class'] = iris.target


# 숫자를 글자로 바꿔보기
df['class'].replace(0, 'flower class 0', inplace=True)
df['class'].replace(1, 'flower class 1', inplace=True)
df['class'].replace(2, 'flower class 2', inplace=True)

# 모양보기
# print(df.shape)

# 첫 10개 값
# print(df.head(10))

# 데이터 갯수, 평균, 분포, Q, 최대, 최소 값 출력
# print(df.describe())

# 그래프 출력해보기
tab = df.groupby('class').size()
# print(eachClassSize)
pct = (tab / tab.sum()) * 100
tab = pd.concat([tab, pct], axis=1)
tab.columns = ['freq', 'percentage']

print(tab)
plt.bar(tab.percentage, tab.freq)
sns.countplot(df['class'])

df.hist()





