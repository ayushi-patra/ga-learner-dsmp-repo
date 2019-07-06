# --------------
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
# code starts here
df = pd.read_csv(path)

# print(df.head())

X = df.loc[:, df.columns != 'list_price']
print(X.head())
print(X.shape)
y = df['list_price']
print(y.head()) 
print(y.shape) 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 6)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape) 

# train, test = train_test_split(df, test_size=0.3) 

# code ends here



# --------------
import matplotlib.pyplot as plt

# code starts here        
cols = X_train.columns
print(cols) 


# fig, axes = plt.subplots(nrows = 3, ncols = 3)

# for i in range(len(cols)):
       
#         for j in range(len(cols)):
#                 col = cols[i * 3 + j]

# plt.scatter(X_train.SalePrice, df.GarageArea)


# for i in cols:
#     for j in cols:
#         col = cols[i * 3 + j]
#         print(col)
#         # plt.scatter(col, ) 



# code ends here



# --------------
# Code starts here
corr = X_train.corr()
print(corr) 
X_train = X_train.drop(['play_star_rating', 'val_star_rating'], axis=1)
print(X_train) 

X_test = X_test.drop(['play_star_rating', 'val_star_rating'], axis=1)
print(X_test) 

# Code ends here


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Code starts here
regressor = LinearRegression()

regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print(y_pred)
mse = mean_squared_error(y_test, y_pred) 
print(mse)
r2 = r2_score(y_test, y_pred)
print(r2) 
# Code ends here


# --------------
# Code starts here

residual = y_test - y_pred
print(residual)


plt.hist(residual)


# Code ends here


