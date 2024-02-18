#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Numpy pandas & Matplotlib

## Data Science-Weekend-Mumbai(Thane)-13th January 2024-09:00 AM to 01:00 PM - Numpy pandas Matplotlib.


# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


pd.read_csv("salaries.csv")


# In[3]:


df = pd.read_csv("salaries.csv")


# In[4]:


df


# In[ ]:





# ## Filtering operation of pandas.

# In[5]:


df


# In[6]:


df.rank


# In[7]:


Assoc_agesal = df[df["rank"] == "AssocProf"]["salary"].mean()


# In[8]:


round(Assoc_agesal,2)


# In[9]:


round(df[df["rank"] == "Prof"]["salary"].mean(),2)


# In[10]:


df[(df["rank"] == "Prof")|(df["rank"] == "AssocProf")] ## Multiple categories being filtered.


# In[11]:


df[(df["rank"] == "AssocProf")&(df["sex"] == "Female")]


# In[12]:


df[(df["rank"] == "AssocProf")&(df["sex"] == "Female")]["salary"].mean() ## Filtering >> average salary


# In[13]:


df[df["salary"]>100000]


# In[14]:


df[(df["salary"]>100000) & (df["rank"]  == "Prof")]


# In[15]:


df.groupby("rank")["salary"].mean()


# In[16]:


df.groupby(["rank","sex"])[["salary","service"]].mean()


# In[17]:


round(df.groupby(["rank","sex"])[["salary","service"]].mean())


# In[18]:


pd.pivot_table(df,values="salary",index="rank")


# In[19]:


pd.pivot_table(df,values="salary",index=["rank","sex"])


# In[20]:


df.sex.value_counts()  ## Count the categories >> How many male & Female are there in the data set


# In[21]:


df["rank"].value_counts()


# In[22]:


df.sort_values("salary",ascending=False)


# In[23]:


df6 = df.sort_values("salary",ascending=False)


# In[24]:


df6.to_csv("df6.csv")


# In[25]:


import os 
os.getcwd()


# In[26]:


df["rank"].unique()


# In[27]:


df["rank"].nunique()


# In[28]:


df["rank"].value_counts()


# In[29]:


df["sex"].value_counts()


# In[30]:


df.value_counts(["rank"])


# In[31]:


df["rank"].min()


# In[32]:


df["rank"].max()


# In[33]:


df["sex"].min()


# In[34]:


df["salary"].min()


# In[35]:


df["salary"].max()


# In[36]:


df.count()


# In[37]:


df.describe()


# In[38]:


df


# In[39]:


df.describe()


# In[ ]:





# In[42]:


df1 =  pd.DataFrame([('Foreign Cinema', 'Restaurant', 289.0, 5.2),
                   ('Liho Liho', 'Restaurant', 224.0, 4.3),
                   ('500 Club', 'bar', 80.5, 3.9),
                   ('The Square', 'bar', 25.30, 1.7)],
           columns=('name', 'type', 'AvgBill', 'Rating')
                 )


# In[43]:


df1


# In[44]:


len("Shubham")


# In[45]:


(df1["name"][0])


# In[46]:


len(df1["name"][0])


# In[47]:


df1["name"].apply(len)


# In[49]:


for i in range(0,4):
    print(len(df1["name"][i]))


# ## List comprehension  :

# In[54]:


fruits = ["apple","banana","pineapple","kiwi","Cherry"]


# In[55]:


[x for x in fruits if "a" in x]


# In[56]:


fruits


# In[57]:


fruits.remove("apple")


# In[58]:


fruits


# In[ ]:





# In[ ]:




