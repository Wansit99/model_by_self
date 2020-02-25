#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


path = 'shizi.jpg'


# In[ ]:


image = cv2.imread(path,cv2.IMREAD_GRAYSCALE)


# In[ ]:


def calcGrayHist(image):
    row,col = image.shape
    GrayHist = np.zeros([256])
    for i in range(row):
        for j in range(col):
            GrayHist[image[i][j]] +=1
    return GrayHist


# In[ ]:


GrayHist = calcGrayHist(image)


# In[ ]:


x_range = range(256)


# In[ ]:


plt.plot(x_range,GrayHist,'r',linewidth='2',c = 'black')


# In[ ]:





# In[ ]:




