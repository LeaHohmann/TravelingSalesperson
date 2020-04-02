#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd


# In[4]:


def dataimport(filename):
    #filename should be CSV with symmetric matrix of the TSP
    data = pd.read_csv(filename,sep=';',index_col=0,engine='python')
    return data


# In[5]:


def salesman(filename):
    data = dataimport(filename)
    if data.size <= 64:
        print("Exact method will be used")
        #Load exact method
        from exact import shortestpath
        distance, shortest = shortestpath(data)
        print("Shortest path: ", shortest)
        print("Length: ", distance)
    else:
        print("I will use a heuristic method to find a best guess as the dataset is larger than 8")
        #Load heuristic method
        from heuristic import findbestroute
        shortest, distance = findbestroute(data)
        print("This is the shortest route I could find with the nearest neighbour method: ", shortest)
        print("Length: ", distance)
    
        #Compare to average, lower limit and upper limit
        print("Here is how it compares:")
        Minlength = 0
        for i in range(len(data)):
            Minlength +=data.iloc[:,i].min()
        print("Sum of distances from each city to nearest neighbour: ",Minlength)
        Maxlength = 0
        for i in range(len(data)):
            Maxlength +=data.iloc[:,i].max()
        print("Sum of distances from each city to farthest neighbour: ",Maxlength)
        Average = len(data)*data.mean().mean()
        print("Average distance of random tour: ",Average)
    return shortest,distance


# In[6]:


#Import salesman and call with salesman.salesman(filename). Filename needs to be CSV and contain a symmetric matrix including the row and column indices!


# In[ ]:





# In[ ]:





# In[ ]:




