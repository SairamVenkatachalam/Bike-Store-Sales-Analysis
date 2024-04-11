#%%
import pandas as pd

filepath='European Bike Sales.csv'
bikes=pd.read_csv(filepath)
# print(bikes.head(10))

numerical_columns = ['Order_Quantity', 'Unit_Cost','Unit_Price', 'Profit', 'Cost', 'Revenue']

Q1 = bikes[numerical_columns].quantile(0.25)
Q3 = bikes[numerical_columns].quantile(0.75)
IQR = Q3 - Q1
def detect_outliers(column):
    lower_bound = Q1[column.name] - 1.5 * IQR[column.name]
    upper_bound = Q3[column.name] + 1.5 * IQR[column.name]
    return (bikes[column.name] < lower_bound) | (bikes[column.name] > upper_bound)

outliers = bikes[numerical_columns].apply(detect_outliers)

print(bikes.shape)
bikes = bikes[~outliers.any(axis=1)]

print(bikes.shape)

#%%

import seaborn as sns
import matplotlib.pyplot as plt
for column in numerical_columns:
    plt.figure()
    sns.boxplot(data=bikes,y=column)
    plt.show()

#%%

bikes.to_csv('Bikes_Filtered.csv', index=False)
