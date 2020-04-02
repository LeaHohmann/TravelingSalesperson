#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import pandas as pd


# In[4]:


def shorteststeps(inputdata,i,cityvector):
    TSP = inputdata.copy()
    pathlength = 0
    node = cityvector[i]
    route = list([node])
    for j in range(len(cityvector)-1):
        pathlength += TSP[node].min()
        route.append(TSP[node].idxmin())
        TSP.loc[node,:] = np.nan
        node = route[j+1]
        j += 1
    return route, pathlength


# In[1]:


def findbestroute(inputdata):
    cityvector = np.array(inputdata.index)
    distance = 10000000
    for i in range(len(cityvector)):
        route, pathlength = shorteststeps(inputdata,i,cityvector)
        if pathlength < distance:
            distance = pathlength
            bestroute = route
        i += 1    
    return bestroute, distance
        


# In[ ]:





# In[ ]:




