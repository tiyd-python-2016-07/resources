# Linear Regression in scikit-learn

import numpy as np
import pandas as pd

# read data into a DataFrame
data = pd.read_csv('advertising.csv', index_col=0)
data.head()

# create X and y
feature_cols = ['TV', 'Radio', 'Newspaper']
X = data[feature_cols]
y = data.Sales

# follow the usual sklearn pattern: import, instantiate, fit
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X, y)

# print intercept and coefficients
print('Intercept:', linreg.intercept_)
print('Coefficient:', linreg.coef_)

# calculate the R-squared
print('R-squared:', linreg.score(X, y))

# pair the feature names with the coefficients
print('Features & Coefficients')
print(list(zip(feature_cols, linreg.coef_)))

# predict for a new observation
new_x = [100, 25, 25]
new_x = np.array(new_x).reshape((1, -1))
print('Prediction:', linreg.predict(new_x))
# result => [12.202667011892373]
