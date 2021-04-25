import pandas as pd
import openpyxl

df = pd.read_csv('src/data/data1.csv')



i = 0
for element in df['a'] :
    if element == 'john' :
        df['name'][i] = 'johnny'
        i += 1

i = 0
for element in df['b'] :
    if element == 25 :
        df['age'][i] = 26
        i += 1


print(df)


