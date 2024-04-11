#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import matplotlib.font_manager as fm
title_font = fm.FontProperties(family='serif', size=16, weight='bold')
label_font = fm.FontProperties(family='serif', size=14)
title_color = 'blue'
label_color = 'darkred'
colormap='Set2'
#%%

# filepath="C:/Users/saira/OneDrive/Desktop/GWU Courses/Semester 2/Data Visualization/Project/Data/European Bike Sales.csv"
filepath='Bikes_Filtered.csv'
bikes=pd.read_csv(filepath)
print(bikes.head(10))

#%%

#-----------------------------------------------------------------------------------
# Lineplot for country wise revenue

sns.set_style("whitegrid")
sns.set_context("notebook")

plt.figure(figsize=(12, 6))

sns.lineplot(x="Year", y="Revenue", hue="Country", data=bikes, estimator='sum', err_style=None)

plt.title("Total Revenue by Year and Country", fontproperties=title_font, color=title_color)
plt.xlabel("Year", fontproperties=label_font, color=label_color)
plt.ylabel("Total Revenue", fontproperties=label_font, color=label_color)
plt.legend(title="Country", loc="upper left", bbox_to_anchor=(1, 1))

# Format x-axis ticks
plt.xticks(bikes['Year'].unique(), rotation=45)

plt.tight_layout()
plt.show()
#%%

sns.set_palette(sns.color_palette('bright'))
plt.figure(figsize=(12, 6))

sns.lineplot(x="Month", y="Revenue", hue="Year", data=bikes, estimator='sum', err_style=None)

plt.title("Total Revenue by Month and Year", fontproperties=title_font, color=title_color)
plt.xlabel("Month", fontproperties=label_font, color=label_color)
plt.ylabel("Total Revenue", fontproperties=label_font, color=label_color)
plt.legend(title="Year", loc="upper left", bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()
#%%


# Revenue vs Profit


sns.set_style("whitegrid")

plt.figure(figsize=(12, 6))

sns.scatterplot(x='Revenue', y='Profit', hue='Country', data=bikes)

plt.title("Revenue vs Profit", fontproperties=title_font, color=title_color)
plt.xlabel("Revenue", fontproperties=label_font, color=label_color)
plt.ylabel("Profit", fontproperties=label_font, color=label_color)
plt.legend(title="Country", loc="upper left", bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()


#%%
country_sales=bikes.groupby('Country')[['Profit', 'Cost', 'Revenue']].sum()
#%%
# Pie chart for share of sales by country
plt.figure(figsize=(18, 12))

# Pie chart for share of sales by country
plt.subplot(2, 2, 1)
sales_by_country = bikes.groupby('Country')['Revenue'].sum()
plt.pie(sales_by_country, labels=sales_by_country.index, autopct='%1.1f%%', colors=plt.cm.get_cmap(colormap)(range(len(sales_by_country))))
plt.title('Share of Revenue by Country', fontproperties=title_font, color=title_color)

# Pie chart for share of sales by country
plt.subplot(2, 2, 2)
sales_by_country = bikes.groupby('Country')['Profit'].sum()
plt.pie(sales_by_country, labels=sales_by_country.index, autopct='%1.1f%%', colors=plt.cm.get_cmap(colormap)(range(len(sales_by_country))))
plt.title('Share of Profit by Country', fontproperties=title_font, color=title_color)

# Clustered chart for sales vs profit by country
plt.subplot(2, 1, 2)
bikes_sales_profit = bikes.groupby('Country')[['Revenue', 'Profit']].sum().reset_index()
sns.barplot(x='Country', y='value', hue='variable',
            data=bikes_sales_profit.melt(id_vars='Country', var_name='variable', value_name='value'),
            palette=colormap)
plt.title('Sales vs Profit by Country', fontproperties=title_font, color=title_color)
plt.ylabel('Amount')
plt.xlabel('Country', fontproperties=label_font, color=label_color)
plt.legend(title=None)

plt.tight_layout()
plt.show()
#%%
# Boxplot by year

plt.figure(figsize=(12, 6))

sns.boxplot(x='Year', y='Profit', data=bikes, palette=colormap)

plt.title('Profit by Year', fontproperties=title_font, color=title_color)
plt.xlabel('Year', fontproperties=label_font, color=label_color)
plt.ylabel('Profit', fontproperties=label_font, color=label_color)

plt.tight_layout()
plt.show()

#%%

# Boxplot of Profit by Country

plt.figure(figsize=(12, 6))

sns.boxplot(x='Country', y='Profit', data=bikes, palette=colormap)

plt.title('Profit by Year', fontproperties=title_font, color=title_color)
plt.xlabel('Country', fontproperties=label_font, color=label_color)
plt.ylabel('Profit', fontproperties=label_font, color=label_color)

plt.tight_layout()
plt.show()

#%%
colormap='Set2'

# Stacked Bar chart


bikes_agg = bikes.groupby(['Year', 'Country'])['Revenue'].sum().unstack()

plt.figure(figsize=(12, 6))
ax = bikes_agg.plot(kind='bar', stacked=True, colormap=colormap)
plt.title("Revenue by year for different countries")
plt.xlabel("Year")
plt.ylabel("Revenue")
plt.legend(title='Country', bbox_to_anchor=(1, 1), loc='upper left')
plt.tight_layout()  # Adjust layout to prevent cutoff
plt.show()


#%%
# Countplot

plt.figure(figsize=(12, 6))
subcat_count = bikes['Sub_Category'].value_counts()
sns.countplot(x='Sub_Category', data=bikes, order=subcat_count.index, palette=colormap)
plt.title('Orders by Sub-Category Count', fontproperties=title_font, color=title_color)
plt.xlabel('Sub-Category', fontproperties=label_font, color=label_color)
plt.ylabel('Count', fontproperties=label_font, color=label_color)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#%%
# Distplots


# Create a distplot for 'Revenue'
plt.figure(figsize=(12, 6))
sns.histplot(bikes['Revenue'], kde=True, color='skyblue')
plt.title('Distribution of Revenue', fontproperties=title_font, color=title_color)
plt.xlabel('Revenue', fontproperties=label_font, color=label_color)
plt.ylabel('Frequency', fontproperties=label_font, color=label_color)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.0f}'.format(x)))
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.2f}'.format(x)))
plt.show()

# Create a distplot for 'Order_Quantity'
plt.figure(figsize=(12, 6))
sns.histplot(bikes['Order_Quantity'], kde=True, color='salmon')
plt.title('Distribution of Order Quantity', fontproperties=title_font, color=title_color)
plt.xlabel('Order Quantity', fontproperties=label_font, color=label_color)
plt.ylabel('Frequency', fontproperties=label_font, color=label_color)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.0f}'.format(x)))
plt.show()

#%%

#Pair plot

numerical_cols = ['Customer_Age', 'Order_Quantity','Profit', 'Cost', 'Revenue']

plt.figure(figsize=(15, 10))
sns.pairplot(bikes[numerical_cols], palette=colormap)
plt.suptitle("Pairplot of Numerical Variables", y=1.02, fontproperties=title_font, color=title_color)
plt.tight_layout()
plt.show()


#%%
# Heatmap


corr = bikes[numerical_cols].corr()

# Create a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', cbar=True)
plt.title("Correlation Heatmap", fontproperties=title_font, color=title_color)
plt.tight_layout()
plt.show()


#%%
# Histogram with KDE


plt.figure(figsize=(12, 8))
sns.histplot(bikes['Customer_Age'], kde=True, color='skyblue', bins=20)
plt.title("Histogram with KDE for Customer Age", fontproperties=title_font, color=title_color)
plt.xlabel("Customer Age", fontproperties=label_font, color=label_color)
plt.ylabel("Frequency", fontproperties=label_font, color=label_color)
plt.tight_layout()
plt.show()

#%%
from statsmodels.graphics.gofplots import qqplot
fig, ax = plt.subplots(figsize=(8, 8))

# QQ plot for Revenue
qqplot(bikes['Revenue'], line='s', ax=ax)
ax.set_title("QQ Plot for Revenue", fontproperties=title_font, color=title_color)
ax.set_xlabel("Theoretical Quantiles", fontproperties=label_font, color=label_color)
ax.set_ylabel("Sample Quantiles", fontproperties=label_font, color=label_color)
plt.show()

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# QQ plot for Quantity
qqplot(bikes['Order_Quantity'], line='s', ax=ax)
ax.set_title("QQ Plot for Quantity", fontproperties=title_font, color=title_color)
ax.set_xlabel("Theoretical Quantiles", fontproperties=label_font, color=label_color)
ax.set_ylabel("Sample Quantiles", fontproperties=label_font, color=label_color)
plt.show()

#%%

# KDE with fill

palette = 'muted'

plt.figure(figsize=(12, 8))
sns.kdeplot(bikes['Customer_Age'], fill=True, alpha=0.6, palette=palette, linewidth=2.5)
plt.title("KDE Plot of Customer Age", fontproperties=title_font, color=title_color)
plt.xlabel("Customer Age", fontproperties=label_font, color=label_color)
plt.ylabel("Density", fontproperties=label_font, color=label_color)
plt.tight_layout()
plt.show()

#%%

# Create a scatter plot with regression line and colormap


#%%

# Boxen plot

plt.figure(figsize=(12, 8))
sns.boxenplot(x='Year', y='Revenue', hue='Country', data=bikes,color='Country', palette=colormap)
plt.title("Multivariate Boxen Plot of Revenue by Year and Country", fontproperties=title_font, color=title_color)
plt.xlabel("Year", fontproperties=label_font, color=label_color)
plt.ylabel("Revenue", fontproperties=label_font, color=label_color)
plt.legend(title="Country", loc="upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()

#%%

revenue_by_year = bikes.groupby('Year')['Revenue'].sum()

# Create an area plot
plt.figure(figsize=(12, 8))
plt.fill_between(revenue_by_year.index, revenue_by_year.values, color='skyblue', alpha=0.6)
plt.plot(revenue_by_year.index, revenue_by_year.values, color='Slateblue', alpha=0.6)
plt.title("Area Plot of Revenue by Year", fontproperties=title_font, color=title_color)
plt.xlabel("Year", fontproperties=label_font, color=label_color)
plt.ylabel("Revenue", fontproperties=label_font, color=label_color)
plt.tight_layout()
plt.show()

#%%

# Violin plot

plt.figure(figsize=(12, 8))
sns.violinplot(x='Customer_Gender', y='Revenue', data=bikes, palette='muted')
plt.title("Violin Plot of Revenue by Customer Gender", fontproperties=title_font, color=title_color)
plt.xlabel("Gender", fontproperties=label_font, color=label_color)
plt.ylabel("Revenue", fontproperties=label_font, color=label_color)
plt.tight_layout()
plt.show()


#%%

sns.jointplot(x='Customer_Age', y='Revenue', data=bikes, kind='kde', color='skyblue')
plt.suptitle("Joint Plot of Customer Age and Revenue", fontproperties=title_font, color=title_color)
plt.xlabel("Customer Age", fontproperties=label_font, color=label_color)
plt.ylabel("Revenue", fontproperties=label_font, color=label_color)
plt.tight_layout()
plt.show()
