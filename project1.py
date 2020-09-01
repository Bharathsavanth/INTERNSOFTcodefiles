# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 14:28:26 2020

@author: Bharath Savanth
"""

#IMPORTING THE LIBRABIES

import pandas as pd
import matplotlib.pyplot as plt


# READING THE DATA FROM YOUR FILE

data = pd.read_csv("advertising.csv")
data.head()

#TO VISUALISE DATA

fig , axs = plt.subplots(1,3,sharey = True)
data.plot(kind='scatter',x='TV',y='Sales',ax=axs[0],figsize=(1,14))
data.plot(kind='scatter',x='Radio',y='Sales',ax=axs[1])
data.plot(kind='scatter',x='Newspaper',y='Sales',ax=axs[2])

#CREATING X&Y FOR LINEAR REGRESSION

feature_cols = ['TV']
X = data[feature_cols]
Y = data.Sales

#IMPORTING LINEAR REGRESSION ALSO FOR SIMPLE LINEAR REGRESSION

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X,Y)

print(lr.intercept_)
print(lr.coef_)

y= a+bx

result = 6.97+0.0554*50
print(result)


# CREATING  A DATAFRAME WITH MIN AND MAX VALUE OF THE TABLE
X_new = pd.DataFrame({'TV':[data.tv.min(),data.tv.max()]})
X_new.head()

preds = lr.predict(X_new)
preds

data.plot(kind='scatter',x='TV',y='Sales')
plt.plot(X_new,preds,c='red',linewidth = 3)

lr = smf.ols(formula ='Sales ~ TV',data = data.fit())
lr.conf_int()

#FINDING THE PROBABALITY VALUES

lm.pvalues

#FINDING THE r-SQUARED VALUES

lm.rsquared

#MULTI LINEAR REGRESSION

feature_cols = ['TV','Radio','Newspaper']
X = data[feature_cols]
y = data.Sales

lr = LinearRegression()
lr.fit(X,y)

print(lr.intercept_)
print(lr.coef_)

lm = smf.ols(formula='Sales ~ TV+Radio+Newspaper',data=data).fit()
lm.conf_int()
lm.summary()