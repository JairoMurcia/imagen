# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 10:37:52 2019

@author: Estudiantes
"""

import numpy as np
from PIL import Image
import random as rn


    



im = Image.open("foto.jpg")
col =  im.size[0] - im.size[0]%4

row=im.size[1]-im.size[1]%4
data = np.zeros((row,col))

pixels =np.array(im)



for i in range(row):
    
    for j in range(col):
        r =  pixels[i,j,0]
      
        data[i,j] = r
        
        
        
aux=np.zeros((row,col)).reshape(16,row//4,col//4)


for i in range (16):
    if i <4:
     aux[i]=data[i*row//4:i*row//4+row//4,0:col//4]
    elif i < 8:
       aux[i]=data[i%4*row//4:i%4*row//4+row//4,0:col//4] 
      
    elif i < 12:
        aux[i]=data[i%8*row//4:i%8*row//4+row//4,0:col//4] 
    else:
        aux[i]=data[i%12*row//4:i%12*row//4+row//4,0:col//4] 

aux1=np.zeros((row//4,col//4))
lista=[]
for i in range(16):
    num=rn.randint(-1,15)
    if  not(i in lista) and not(num in lista) :
        aux1[:]=aux[i:i+1,:,:]
        aux[i]=aux[num]
        aux[num:num+1,:,:]=aux1[:]
        lista.append(num)
        lista.append(i)
    if not(i in lista ):
        while num in lista:
            num=rn.randint(-1,15)
        aux1[:]=aux[i:i+1,:,:]
        aux[i]=aux[num]
        aux[num:num+1,:,:]=aux1[:]
        lista.append(num)
        lista.append(i)    
            


for i in range (4):
    array1=np.hstack((array1,aux[i]))

        
    
        
        