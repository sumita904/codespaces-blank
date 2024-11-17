import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

data= pd.read_csv('2014_apple_stock.csv')
data['AAPL_x']=pd.to_datetime(data['AAPL_x'])
print("The first five rows of the dataset")
print(data.head())
print("\n statistics")
print(data.describe())
plt.figure(figsize=(10,6))
plt.plot(data['AAPL_x'],data['AAPL_y'],label='Apple Stock',color='blue')
plt.xlabel('Date')
plt.ylabel('Stock price(USD)')
plt.title('Apple Share Prices over Time 2014')
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()