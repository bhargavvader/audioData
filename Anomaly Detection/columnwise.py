import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

df = pd.read_csv('dumps.csv')

df = df.drop('index', 1)

df = df[df.power != 'power']

df = df.convert_objects(convert_numeric = True)

# print(df.corr())

# print(df.weight1.min(), df.weight1.max())
# print(df.weight2.min(), df.weight2.max())
# print(df.weight3.min(), df.weight3.max())
# print(df.pos1.min(), df.pos1.max())
# print(df.pos2.min(), df.pos2.max())
# print(df.pos3.min(), df.pos3.max())
# print(df.power.min(), df.power.max())

# print(df.weight2.std())
# print(df.weight3.std())
# print(df.pos1.std())
# print(df.pos2.std())
# print(df.pos3.std())
# print(df.power.std())

#print(df)

df_norm = (df - df.mean())/df.std()

x = df_norm**2 - (df_norm.std()*3)**2 >= 0

print((x==1).sum())

# print(df)

# print(df.corr())

# print(df.weight1.min(), df.weight1.max())
# print(df.weight2.min(), df.weight2.max())
# print(df.weight3.min(), df.weight3.max())
# print(df.pos1.min(), df.pos1.max())
# print(df.pos2.min(), df.pos2.max())
# print(df.pos3.min(), df.pos3.max())
# print(df.power.min(), df.power.max())

# print(df.weight2.std())
# print(df.weight3.std())
# print(df.pos1.std())
# print(df.pos2.std())
# print(df.pos3.std())
# print(df.power.std())

# mat = df.as_matrix()

# km = KMeans(n_clusters=5)
# km.fit(mat)

# labels = km.labels_

# results = pd.DataFrame([df.index, labels]).T

# print(results[1])