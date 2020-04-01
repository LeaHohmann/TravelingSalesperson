#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from itertools import permutations
import numpy as np
import pandas as pd
    


# In[ ]:


def shortestpath(inputdataframe):
    pathvector = np.array(inputdataframe.index)
    permutating_vector = pathvector[:-1]
    distance = 1000000
    for permutating_path in permutations(permutating_vector,len(permutating_vector)):
        path = np.append(permutating_path,pathvector[-1])
        rearrangeddata = inputdataframe.reindex(path,axis='columns')
        rolledpath = np.roll(path,len(path)-1)
        rearrangeddata = rearrangeddata.reindex(rolledpath,axis='index')
        pathlength = np.sum(np.diagonal(rearrangeddata))
        if pathlength < distance:
                distance = pathlength
                shortest = path 
    return distance, shortest
            

        

