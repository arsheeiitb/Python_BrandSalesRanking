#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


sales_df = pd.read_csv('Sales.csv')
product_df = pd.read_csv('Product.csv')


# In[3]:


sales_product_df = pd.merge(sales_df, product_df, on='ProductCode')

grouped_df = sales_product_df.groupby(['BrandName', 'ProductName'])

total_sales_df = grouped_df['Sales'].sum().reset_index()

total_sales_df['Rank'] = total_sales_df.groupby('BrandName')['Sales'].rank(ascending=False)

result_df = total_sales_df[total_sales_df['Rank'] == 1]

print(result_df)


# In[ ]:




