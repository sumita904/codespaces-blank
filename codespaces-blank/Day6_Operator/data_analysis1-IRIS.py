import pandas as pd
import matplotlib.pyplot as plt
from fontTools.subset import subset

data= pd.read_csv('iris.csv')
print("The first five rows of the dataset")
print(data.head())
print("\n statistics")
print(data.describe())
plt.figure(figsize=(8,5))

for variety,color in zip(data['variety'].unique(),['r','g','b']):
    subset=data[data['variety']==variety]
    plt.scatter(subset['sepal.length'],subset['sepal.width'],label=variety,color=color)
plt.xlabel('sepal.length')
plt.ylabel('sepal.width')
plt.title('sepal.length vs sepal.width')
plt.legend()
plt.grid(True)
plt.show()
