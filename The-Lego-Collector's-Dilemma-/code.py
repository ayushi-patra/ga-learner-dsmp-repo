# --------------
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split

# code starts here
df = pd.read_csv(path)
print(df.head())

X = df.loc[:, df.columns != 'list_price']
print(X.head())
print(X.shape)

y = df['list_price']
print(y.head()) 
print(y.shape) 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 6)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape) 


# Correlation Check
import matplotlib.pyplot as plt
       
cols = X_train.columns

fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(20,20))

for i in range(0,3):             #iterating the row
    for j in range(0,3):         # iterating the column
            col = cols[i*3 + j]
            axes[i,j].set_title(col)
            axes[i,j].scatter(X_train[col],y_train)
            axes[i,j].set_xlabel(col) 
            axes[i,j].set_ylabel('list_price')


# Reduce feature redundancies!
corr = X_train.corr()
print(corr) 

X_train = X_train.drop(['play_star_rating', 'val_star_rating'], axis=1)
print(X_train) 

X_test = X_test.drop(['play_star_rating', 'val_star_rating'], axis=1)
print(X_test) 


# Price Prediction 

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

regressor = LinearRegression()

regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print(y_pred)

mse = mean_squared_error(y_test, y_pred) 
print(mse)

r2 = r2_score(y_test, y_pred)
print(r2) 

# Residual Check 
residual = y_test - y_pred
print(residual)

# Visualize 
plt.hist(residual)


# Code ends here
