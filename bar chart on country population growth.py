#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import bar_chart_race as bcr


# In[3]:


df = pd.read_csv("https://raw.githubusercontent.com/dexplo/bar_chart_race/master/data/urban_pop.csv")


# In[4]:


df.head()


# In[5]:


df = df.set_index('year')


# In[6]:



df.head()


# In[7]:


df.columns


# In[11]:


bcr.bar_chart_race(df = df, title = "Population Growth")

