import numpy as np                                     #for data handling and manipulating
import pandas as pd                                     #for data handling and manipulating
import matplotlib.pyplot as plt                        # for visualizing data and model
from sklearn.model_selection import train_test_split    #to split data for training and testing
from sklearn.linear_model import LinearRegression      #build and train the regression model
from sklearn.metrics import mean_squared_error         # evaluate model's performance

data = {
    "size":[900,850,1200,1000,1500,1800,2000],
    "price":[100,95,125,110,150,180,200]
}
df = pd.DataFrame(data)
x = df[["size"]]   #predictor
y = df[["price"]]  #target

X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.2, random_state=42)
print(f"print X Training data:{X_train}\n")
print(f"print Y Training data:{Y_train}")

model = LinearRegression()
model.fit(X_train,Y_train)                  #to train the model using the training data
print("Model trained successfully")

Y_pred = model.predict(X_test)              #predicting the model
print("predicted values",Y_pred)
print("Actual values",Y_test.values)

mse = mean_squared_error(Y_test,Y_pred)
print("mean squared error:",mse)
print("slope:",model.coef_[0])

plt.scatter(x,y,color="blue",label="Actual Data")
plt.plot(x,model.predict(x),color="red",label="Regression Line")
plt.title("House size vs Price")
plt.xlabel("size(sqft)")
plt.ylabel("price(1000s)")
plt.legend()
plt.show()
