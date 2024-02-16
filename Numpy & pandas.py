#!/usr/bin/env python
# coding: utf-8

# ## Python : - Pandas & Numpy 
# 

# In[30]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:





# In[31]:


import numpy as np
import matplotlib.pyplot as plt


# ## Array

# In[32]:


l1 = [1,2,3]


# In[33]:


l1


# In[34]:


array = np.array([1,2,3,"a"])


# In[35]:


array ## One dimentional array.


# In[36]:


array[0] ## Index position


# In[37]:


array.shape ## To show the colunm 


# In[38]:


array.ndim  ## Check that how much dimension your arraya have 


# In[39]:


plt.plot(array,"bo")


# In[40]:


array = np.array([[1,2,3],[4,5,6]]) ## Two dimentional array


# In[41]:


array ## Dimension 


# In[42]:


array.shape


# In[43]:


array.ndim


# In[44]:


plt.plot(array,"bo") ## Only visulize two dimentional array & one dimentional array


# In[45]:


print(type(array))


# In[46]:


## Three dimentional array


# In[47]:


a1 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])


# In[48]:


a1


# In[49]:


a1.shape


# In[50]:


a1.ndim


# In[ ]:





# In[51]:


array = np.array([[1,2,3],[4,5,6]])


# In[52]:


array


# In[53]:


np.array([1,2,3])


# In[54]:


array = np.array([1,2,3])


# In[55]:


array


# ## Series 

# In[56]:


pd.Series(array)


# In[57]:


print(list(range(1,100)))


# In[58]:


Ser1 = pd.Series(range(1,100))


# In[59]:


Ser1[90]


# In[60]:


Ser1


# In[61]:


d = {"a":1,"b":2,"c":3}
Ser = pd.Series(d)
Ser


# In[62]:


d1 = [1,2,3]
Ser1 = pd.Series(d1,index=["a","b","c"])
Ser


# ## Data Frame

# In[63]:


pd.DataFrame()


# In[64]:


pd.DataFrame(data=[[1,2,3],[4,5,6]],index = ["x","y"],columns = ["a","b","c"])


# In[65]:


pd.Series(data=[1,2,3])


# In[66]:


pd.DataFrame(data=[[1,2,3],[4,5,6]],index = ["x","y"], columns = ["a","b","c"])


# In[ ]:





# In[67]:


import os 
os.getcwd()


# In[68]:


pd.read_csv("salaries.csv")


# In[69]:


df = pd.read_csv("salaries.csv")


# In[70]:


df


# In[71]:


df.head()


# In[72]:


df.tail(10)


# In[73]:


x = [1,2,3]


# In[74]:


print(type(x))


# In[75]:


type(df)


# In[76]:


df.head()


# In[77]:


df.describe()


# In[78]:


df.describe(include="all")


# In[81]:


df.sample(3)


# In[83]:


df.sample(13,replace=True)


# In[86]:


df.sample(13,random_state=42)


# In[88]:


df.dropna()


# In[91]:


df.info()


# In[94]:


df.phd = df.phd.astype("int32")


# In[95]:


df.info()


# In[96]:


df.ndim


# In[97]:


df.columns


# In[98]:


df.size


# In[99]:


df.shape


# ## Selecting columns

# In[100]:


df.salary    ## Single column slicing   


# In[101]:


type(df.salary)


# In[103]:


df["rank"]


# In[106]:


df [["salary","sex","service"]] ## For multiple slicing >> Need to use double bracket. other wise it will give error.


# In[108]:


df.head(78)


# In[110]:


df.iloc[5:10] ## It will use to access the row from the data set


# In[111]:


df.iloc[5:10,0:2]


# In[112]:


df.iloc[:,0:2]


# In[114]:


df.loc[0]


# In[115]:


df.iloc[0:10] ## Lable >> Both are same 


# In[116]:


df.loc[0:10] ## Index >> Both are same 


# In[118]:


df.loc[10:15,["rank","discipline"]]


# ## To be continue in next notebook 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




