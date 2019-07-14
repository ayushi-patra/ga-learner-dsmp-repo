import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# path- variable storing file path

#Code starts here

# load the dataframe
df = pd.read_csv(path)

#Indepenent varibles
X = df.drop('Price',axis=1)

# store dependent variable
y = df['Price']

# spliting the dataframe

X_train,X_test,y_train,y_test=train_test_split(X,y ,test_size=0.3,random_state=6)

# check correlation
corr=X_train.corr()

# print correlation
print(corr)

# ======================================================
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Code starts here

#Instantiate linear regression model
regressor=LinearRegression()

# fit the model
regressor.fit(X_train,y_train)

# predict the result
y_pred =regressor.predict(X_test)


# Calculate r2_score
r2 = r2_score(y_test, y_pred)

#print r2
print(r2)

# Code ends here

# ======================================================
from sklearn.linear_model import Lasso

# Code starts here

# instantiate lasso model
lasso = Lasso()

# fit and predict
lasso.fit(X_train, y_train)
lasso_pred = lasso.predict(X_test)

# calculate RMSE
r2_lasso = r2_score(y_test, lasso_pred)
print (r2_lasso)

# Code ends here

# =====================================================
from sklearn.linear_model import Ridge

# Code starts here

# instantiate lasso model
ridge = Ridge()

# fit and predict
ridge.fit(X_train, y_train)
ridge_pred = lasso.predict(X_test)

# calculate RMSE)
r2_ridge = r2_score(y_test, ridge_pred)
print (r2_ridge)

# Code ends here

# =====================================================
from sklearn.model_selection import cross_val_score

#Code starts here

# Initiate Linear Regression Model
regressor=LinearRegression()

# Initiate cross validation score
score= cross_val_score(regressor,X_train,y_train ,scoring= 'r2' ,cv=10)
print(score)
#calculate mean of the score
mean_score = np.mean(score)

# print mean score
print(mean_score)


#Code ends here

# =====================================================
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# make pipeline for second degree polynomialfeatures
model = make_pipeline(PolynomialFeatures(2), LinearRegression())

# Fit the model on training set
model.fit(X_train, y_train)

# predict the model performance
y_pred = model.predict(X_test)

# calculate r2 score
r2_poly= r2_score(y_test,y_pred)

# print r2 score
print(r2)
