import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
absolute_path = os.path.abspath(os.path.dirname('pollution_data.csv'))
df = pd.read_csv(absolute_path + '/pollution_data.csv')
df1 = df[['deviceid', 'pm25','x', 'y']]
#print(df1.head())
heatmap1_data = pd.pivot_table(df1, values='pm25', index='y', columns = 'x')
fig = sns.heatmap(heatmap1_data, cmap="YlOrBr")
fig.invert_yaxis()
plt.show()
'''
#print(df.head(10))
symbol = np.asarray(df['deviceid'])
percentage = np.asarray(df['pm25'])
#print(symbol)
#print(percentage)
#result = df.pivot(index='y', columns='x', values='pm25')
#print(result)
#labels = np.asarray["{0} \n {1:.2f}".format(symb,value) for symb, value in zip(sybmol, percentage)]
fig, ax = plt.subplots(figsize=(12,7))
title = "Pollution at IIT Delhi Heatmap"
plt.title(title, fontsize=18)
ttl = ax.title
ttl.set_position([0.5,1.05])
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')
sns.heatmap(result,annot=labels,fmt="",cmap='RdYlGn',linewidths=0.30,ax=ax)
plt.show()
'''