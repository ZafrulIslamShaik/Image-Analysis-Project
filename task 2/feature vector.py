#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
# function for template matching
def template_matching_NCC (src, temp):
    # obtaining the height and width of the image
    h_src, w_src = src.shape
    # obtaining the height and width of the template
    ht_temp, wt_temp = temp.shape
    # array for storing the differences
    diff = np.empty((h_src - ht_temp, w_src - wt_temp))
    src = np.array(src, dtype="float")
    temp = np.array(temp, dtype="float")
    # searching for template in the image
    for dy in range(0, h_src - ht_temp):
        for dx in range(0, w_src - wt_temp):
            # for obtaining absolute sum of differences
            r_o_i = src[dy:dy + ht_temp, dx:dx + wt_temp]
            numerator = np.sum(r_o_i * temp)
            denominator = np.sqrt((np.sum(r_o_i ** 2))) * np.sqrt(np.sum(temp ** 2))
            if denominator == 0 : diff[dy, dx] = 0
            diff[dy, dx] = numerator / denominator

    NCC_Max = np.max(diff)
    print(NCC_Max)

    # returns the searched position with the lowest difference
    pt = np.unravel_index(diff.argmax(), diff.shape)
    # return (pt[1], pt[0])
    return NCC_Max


# In[14]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Assigning path for images
dirpath="Z:\img analysis project final\images/"
exepath=".jpg"
NCC_Matrix=np.zeros((6,6))

for i in range(1,7):
    for j  in range(1,7):
        sourceImage = cv2.imread(dirpath + str(i)+ exepath)
        templateImage = cv2.imread(dirpath + str(j)+ exepath)


    # scaling the template
        IMG_SIZE = 31
        resizedTemp = cv2.resize(templateImage, (IMG_SIZE, IMG_SIZE))
    # cv2.imshow("template image",new_array)

        gray = cv2.cvtColor(sourceImage, cv2.COLOR_RGB2GRAY)
        templateImage1 = cv2.cvtColor(resizedTemp, cv2.COLOR_RGB2GRAY)
        h_temp, w_temp = templateImage1.shape

    # call of template matching function
        NCC_Matrix[i-1][j-1] = template_matching_NCC(gray, templateImage1)


# obtaing the values for feature vector 
Array= [1,2,3,4,5,6]
row0 = [row[0] for row in NCC_Matrix]
row1 = [row[1] for row in NCC_Matrix]
row2 = [row[2] for row in NCC_Matrix]
row3 = [row[3] for row in NCC_Matrix]
row4 = [row[4] for row in NCC_Matrix]
row5 = [row[5] for row in NCC_Matrix]

A  = np.array(Array)
B1 = np.array(row0)
B2 = np.array(row1)
B3 = np.array(row2)
B4 = np.array(row3)
B5 = np.array(row4)
B6 = np.array(row5)

# plotting the graph of feature vector
plt.scatter(A,B1,marker = '*',color = 'blue',label = 'Image1')
plt.scatter(A,B2,marker = '+',color = 'blue',label = 'Image2')
plt.scatter(A,B3,marker = '^',color = 'red',label = 'Image3' )
plt.scatter(A,B4,marker = '_',color = 'red' ,label = 'Image4')
plt.scatter(A,B5,marker = '|',color = 'blue',label = 'Image5')
plt.scatter(A,B6,marker = 'x',color = 'red'  ,label = 'Image6')
plt.legend(fancybox = True, framealpha = 1,shadow = True,loc = 'lower left')

plt.title(' Plot of Feature Vectors')
plt.xlabel(' Visual Words  --------> X')
plt.ylabel('NCC --------> Y')
plt.show()



# In[ ]:





# In[ ]:





# In[ ]:




