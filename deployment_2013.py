#!/usr/bin/env python
# coding: utf-8

# In[47]:


#Importing Libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings("ignore")


# In[37]:


#Loading dataset
df = pd.read_csv('Netflix Engagement (plus).csv')
df.sample(10)


# In[38]:


#Shape of dataset
df.shape


# In[39]:


#Checking Columns of dataset
df.columns


# In[40]:


#First 5 rows of dataset
df.head(5)


# In[41]:


#Last 5 rows of dataset
df.tail(5)


# In[42]:


#describing the dataset
df.describe()


# In[43]:


df.describe(include = 'all')


# In[44]:


#Checking null values
df.isnull().sum()


# In[45]:


#total number of unique values
for i in df.columns:
    
    BOLD = "\033[1m"
    RESET = "\033[0m"
    print(BOLD + i + RESET)
    
    print(df[i].nunique(), '\n')


# In[46]:


df.info()


# In[82]:


#Changing datatype
df['Release Date'] = pd.to_datetime(df['Release Date'])
df['Number of Ratings'] = np.int64(df['Number of Ratings'])


# In[52]:


#describing info after changing datatype
df.info()


# In[53]:


df["Available Globally"] = df["Available Globally?"]
df.drop(columns=("Available Globally?"), axis = 1, inplace = True)


# In[54]:


df.sample(3)


# In[55]:


#adding new columns
df['Release Year'] = df['Release Date'].dt.year.fillna(0).astype('int64')
df['Release Month'] = df['Release Date'].dt.month.fillna(0).astype('int64')
df['Release Day'] = df['Release Date'].dt.day_name()


# In[58]:


df.sample(3)


# In[59]:


df.isnull().sum()


# In[60]:


df['Release Day'].fillna('Unknown', inplace = True)


# In[61]:


df['Number of Ratings'].max()


# In[62]:


df['Number of Ratings'].min()


# In[63]:


df[df['Number of Ratings'] <= 0]['Number of Ratings'].count()


# In[65]:


df[df['Number of Ratings'] <= 0]['Number of Ratings'].nunique()


# In[66]:


df_with_ratings = df.loc[df['Number of Ratings'] > 0]
df_with_ratings.sample(3)


# In[67]:


df_with_ratings.shape


# In[68]:


top_10_shows = df_with_ratings.sort_values('Hours Viewed', ascending= False).head(10)
top_10_shows


# In[70]:


# Visualizing top 10 most viewed movies
import seaborn as sns
plt.figure(figsize=(10, 6))

sns.barplot(x='Hours Viewed', y='Title', data=top_10_shows)
plt.title('Top 10 Most Viewed Netflix Shows (Jan-Jun 2023)')
plt.xlabel('Hours Viewed (in 100 Millions)')
plt.ylabel('Titles')
plt.show()


# In[71]:


# Number of ratings 
df_with_ratings[df_with_ratings['Number of Ratings'] < 100].shape


# In[72]:


# top 10 most rated movies
top_ratted_show = df_with_ratings[df_with_ratings['Number of Ratings'] > 1000].sort_values('Rating', ascending=False).head(10)
top_ratted_show


# In[73]:


# top 10 most rated movies in 2023.
top_ratted_show_23 = df_with_ratings[(df_with_ratings['Number of Ratings'] > 1000) & (df_with_ratings['Release Year'] == 2023)].sort_values('Rating', ascending = False).head(10)
top_ratted_show_23


# In[74]:


# Top 10 most Rated Netflix Movies w.r.t. Hours Viewed.
plt.figure(figsize=(8, 8))
plt.pie(top_ratted_show_23['Hours Viewed'], labels=top_ratted_show_23['Title'], autopct='%1.1f%%')
plt.title('Distribution of Viewership Among Top 10 Highest Rated Netflix Shows/Movies')
plt.show()


# In[75]:


# Visualizing Viewership Across Release Years
plt.figure(figsize=(12, 6))
sns.boxplot(x='Release Year', y='Hours Viewed', data=df_with_ratings)
plt.xlabel('Release Year')
plt.ylabel('Hours Viewed')
plt.title('Viewership Across Release Years')
plt.show()


# In[76]:


# Shows available globally
sns.countplot(x='Available Globally', data=df_with_ratings)
plt.title('Count of Movies/Shows Available Globally')
plt.show()


# In[77]:


# % of movies available globally
global_counts = df_with_ratings['Available Globally'].map({'Yes': 1, 'No': 0}).value_counts()

plt.figure(figsize=(8, 8))
plt.pie(global_counts, labels=global_counts.index, autopct='%1.1f%%', colors=['#48dbfb', '#9980FA'])
plt.title('Count of Movies Available Globally')
plt.legend(labels=['Yes', 'No'], loc='upper right')
plt.show()


# In[78]:


# Released movie timeline
df_with_ratings['Release Date'] = pd.to_datetime(df_with_ratings['Release Date'], errors='coerce')

plt.figure(figsize=(12, 6))
sns.histplot(df_with_ratings['Release Date'], bins=20, kde=True, color='salmon')
plt.xlabel('Release Date')
plt.ylabel('Frequency')
plt.title('Distribution of Release Dates')
plt.show()


# In[ ]:




