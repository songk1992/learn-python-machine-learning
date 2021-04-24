
# 노인인구 분석
# https://www.data.go.kr/data/15056374/fileData.do

# csv 파일을 읽어 봅시다

import pandas as pd

df = pd.read_csv('src/data/open_data_jeju_senior_population_20200102.csv')

# 데이터 출력
# print(df.to_string())

# 최상단에 10개만 출력
# print(df.head(10))

# 데이터 정보 출력
# print(df.info())