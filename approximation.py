#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd


# In[2]:


def shorteststeps(inputdata,i,indexvector):
    length = 0
    x = i
    path = np.zeros(len(indexvector))
    For j in range(len(indexvector)-1):
        pathlength += inputdata[x].min()
        path[j] = inputdata[x].idxmin()
        inputdata[x:x+1] = np.nan
        x = np.where(cityvector == path[j])
        j +=1
    return path, pathlength

        


# In[ ]:


def findbestroute(inputdata):
    cityvector = np.array(inputdata.index)
    distance = 10000000
    For i in range(len(cityvector)):
        path, pathlength = shorteststeps(inputdata,i,cityvector)
        if pathlength < distance:
            distance = pathlength
            bestroute = path
        i += 1
    return bestroute, distance
        

