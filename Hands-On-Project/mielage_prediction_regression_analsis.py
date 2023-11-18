# -*- coding: utf-8 -*-
"""Mielage prediction - Regression Analsis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L11CCRUwYSoWaTLtaqcrypCkUT1DVsBy

# TITLE

Mielage prediction

#Obective

to predict Mielage

# Import Library
"""

import pandas as pd

import numpy as np

"""# Import Data"""

df = pd.read_csv('https://raw.githubusercontent.com/YBI-Foundation/Dataset/main/MPG.csv')

df.head()

df.nunique()

"""# Data Preprocessing"""

df.info()

df.describe()

df.corr()

"""# Remove Missing Values"""

df = df.dropna()

df.info()

"""# Data Visualization"""

sns.pairplot(df, x_vars = ['displacement', 'horsepower', 'weight', 'acceleration', 'mpg'], y_vars = 'mpg')

sns.regplot(x = 'displacement', y = 'mpg', data = df)

"""# Define Target Variable y and Feature X"""

df.columns

y = df['mpg']

y.shape

x = df[['displacement', 'horsepower', 'weight', 'acceleration']]

x.shape

"""# Scaling Data"""

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

x = ss.fit_transform(x)

pd.DataFrame(x).describe()

"""# Train Test Split Data"""

from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(x, y, train_size = 0.7)

xtrain.shape, xtest.shape, ytrain.shape, ytest.shape

"""# Linear Regression Model"""

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(xtrain, ytrain)

lr.intercept_

lr.coef_

"""**Mileage = 23.6 - 0.13, Displacemet = -1.42, Horsepower = -5.23, Weight = 0.22 Acceleration + error**

# Predict Test Data
"""

y_pred = lr.predict(xtest)

y_pred

"""# Model Accuracy"""

from sklearn.metrics import mean_absolute_error, r2_score, mean_absolute_percentage_error

mean_absolute_error(ytest, y_pred)

mean_absolute_percentage_error(ytest, y_pred)

r2_score(ytest, y_pred)

"""# Polynomial Regression"""

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree = 2, interaction_only = True, include_bias = False)

x_train2 = poly.fit_transform(xtrain)

x_test2 = poly.fit_transform(xtest)

lr.fit(x_train2, ytrain)

lr.intercept_

lr.coef_

y_pred_poly = lr.predict(x_test2)

"""# Model Accuracy"""

mean_absolute_error(ytest, y_pred_poly)

mean_absolute_percentage_error(ytest, y_pred_poly)

r2_score(ytest, y_pred_poly)

