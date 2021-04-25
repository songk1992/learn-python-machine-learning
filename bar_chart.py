import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('src/data/dataf1.csv')
fig, ax = plt.subplots()
data['Points'].value_counts().plot(ax=ax, kind='bar')