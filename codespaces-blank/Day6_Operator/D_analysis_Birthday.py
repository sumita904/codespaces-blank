import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
data=pd.read_csv('birthdays.csv')
print("The first five rows of birthday")
print(data.head())
plt.figure(figsize=(10,6))
births_per_year= data.groupby('year')['births'].sum()
plt.plot( births_per_year.index, births_per_year.values,color='green')
plt.xlabel('Yearwise')
plt.ylabel('No. of Births')
plt.title('Birthday graph statewise')
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.xticks(births_per_year.index)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

