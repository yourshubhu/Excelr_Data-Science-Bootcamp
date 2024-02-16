#!/usr/bin/env python
# coding: utf-8

# ## Excelr : Python 
# ###### 28-01-2024 09:00 AM Batch
# 

# ## Day 3 Python series dataframes pandas 

# In[7]:


print("Welcome to excelr data science course")


# In[8]:


x=1


# In[9]:


id(x)


# In[10]:


type(x)


# ## Important website : - Stack overflow : -
# ###### For any error detection in program.

# In[11]:


y=2.5


# In[12]:


type(y)


# In[16]:


z="Excelr"


# In[14]:


type(z)


# In[18]:


print(type(z))


# In[20]:


w = True 


# In[21]:


type(w)


# In[22]:


print(type(w))


# ##### del(type) use to delete the error blocks.

# ## Data structure : -

# # Tuple

# In[23]:


x = "a","b","c","d"


# In[24]:


print(x)


# In[25]:


type(x)


# In[26]:


x[0]


# In[27]:


x[1]


# In[28]:


x[2]


# In[29]:


x[3]


# ## Slicing : -

# In[32]:


x[0:2]


# In[33]:


x[1:3]


# In[38]:


x[0],x[2]


# In[41]:


x.index("a")


# In[45]:


x.index("c")


# In[46]:


w = 1,2,3


# In[47]:


print(w)


# In[48]:


type(w)


# In[ ]:





# ## List

# In[43]:


y = [1,2,3]


# In[44]:


type(y)


# In[49]:


y[2]


# In[50]:


y[0:2]


# In[51]:


y[0] = 4 ## Modification is pissible 


# In[ ]:





# ## Dictionary 

# In[52]:


dictionary = {"a":1,"b":2,"c":3}


# In[53]:


dictionary["b"]


# In[54]:


dictionary ["a"] = 4


# In[55]:


dictionary 


# In[ ]:





# ## Write user defined fuctions.

# In[59]:


def Hello():
    print("Hello Excelr")


# In[60]:


Hello()


# In[64]:


def my_age(x):
    print(my_age is:',x)


# In[65]:


2**3


# In[75]:


import numpy as np


# In[76]:


np.square(4)


# In[1]:


def square(x,y):
    return x**2,y**2


# In[4]:


square(2,3)


# In[5]:


sq


# In[11]:


def func(a,*,b,c):
    pass

## Positional argument   ## Keyword argument.


# In[12]:


func(1,b=2,c=3)


# In[ ]:





# ## Methods Functions.

# In[19]:


shop_list = ["Apple","Soap","Bread","Jam","Shampu"]


# In[20]:


shop_list


# In[21]:


shop_list [5] = "Butter"


# In[16]:


dir(list)

## Methods :

'append',
 'clear',
 'copy',
 'count',
 'extend',
 'index',
 'insert',
 'pop',
 'remove',
 'reverse',
 'sort'
# In[22]:


shop_list.append(["butter","Chicken"])


# In[23]:


shop_list


# In[24]:


shop_list.extend(["butter","Chicken"])


# In[25]:


shop_list


# In[27]:


shop_list.pop()


# In[28]:


shop_list


# In[31]:


shop_list.pop(5)


# In[32]:


shop_list


# In[33]:


shop_list.sort()


# In[34]:


shop_list


# In[ ]:





# In[29]:


def func(a,**kwargs):
    pass


# In[30]:


func(1,b = 2,c = 3,d = 4)


# In[ ]:





# In[35]:


fn = lambda x:x **2


# In[36]:


fn(2)


# ## numpy & pandas start with different notebook

# In[ ]:


#_______________To be continue in next notebook

