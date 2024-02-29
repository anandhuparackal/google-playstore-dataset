#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


# Load the dataset
file_path = '/Users/anandhu/Desktop/assignment1/googleplaystore.csv'
df = pd.read_csv(file_path)


# In[3]:


df


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.info ()


# In[7]:


df.describe()


# In[8]:


df['Category'].value_counts()


# In[9]:


df.loc[df['Category'] == '1.9']


# In[10]:


df = df.drop(10472, axis=0)
df['Type'].value_counts()


# In[11]:


df['Content Rating'].value_counts()


# In[12]:


# Barchart Diagram
category = df['Category'].value_counts()
plt.figure(figsize=(10,10))
plt.title('Category')
sns.barplot(x=category, y=category.index)
plt.show()


# In[13]:


# Clean 'Installs' column by removing commas and converting to numeric
df['Installs'] = df['Installs'].str.replace(',', '').str.extract('(\d+)').astype(float)

# Replace NaN values in 'Installs' with a default value (e.g., 0)
df['Installs'].fillna(0, inplace=True)

average_rating_by_category = df.groupby('Category')['Rating'].mean().reset_index()
# Interactive Scatter Diagram (e.g., Ratings vs. Reviews)
scatter_fig = px.scatter(df, x='Rating', y='Reviews', color='Category', size='Installs', hover_name='App',
                         title='Scatter Diagram of Ratings vs. Reviews')
scatter_fig.write_html('scatter_plot.html')
scatter_fig.show()


# In[14]:


# Matrix Diagram (e.g., Correlation matrix)
# Exclude non-numeric columns before calculating correlation
df = df.drop(columns=['Unnamed: 0'])
numeric_columns = df.select_dtypes(include=[np.number]).columns
correlation_matrix = df[numeric_columns].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()


# In[ ]:




