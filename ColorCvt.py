#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import matplotlib.pyplot as plt


# In[ ]:


path = 'shizi.jpg'


# In[ ]:


image = cv2.imread(path)#BGR
img_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(img_RGB)


# In[ ]:


img_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
plt.imshow(img_HSV)


# In[ ]:


img_LAB = cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
plt.imshow(img_LAB)

