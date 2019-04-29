# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 10:37:52 2019

@author: Estudiantes
"""

import numpy as np
from PIL import Image
import random as rn


    



im = Image.open("prueba.png")
col =  im.size[0] - im.size[0]%4

row=im.size[1]-im.size[1]%4
data = np.zeros((row,col))

pixels =np.array(im)



for i in range(row):
    
    for j in range(col):
        r =  pixels[i,j,0]
      
        data[i,j] = r
        
if row<=col:       
    tam=row//4
    t=row
else:
    tam=col//4
    t=col       
aux=np.zeros((t,t)).reshape(16,tam,tam)

for i in range (16):
    if i <4:
        aux[i]=data[0:tam,i*tam:i*tam+tam]
    elif i < 8:
       aux[i]=data[tam:2*tam,i%4*tam:i%4*tam+tam] 
      
    elif i < 12:
        aux[i]=data[2*tam:3*tam,i%4*tam:i%4*tam+tam] 
    else:
        aux[i]=data[3*tam:,i%4*tam:i%4*tam+tam] 

aux1=np.zeros((tam,tam))

lista=[]

for i in range(16):
    
    num=rn.randint(-1,15)
    while num==i:
         num=rn.randint(-1,15)
    
    if  not(i in lista) and not(num in lista) :
        aux1[:]=aux[i]
        aux[i]=aux[num]
        aux[num]=aux1[:,:]
        lista.append(num)
        lista.append(i)
    if not(i in lista ):
        while num in lista:
            num=rn.randint(-1,15)
        aux1[:]=aux[i]
        aux[i]=aux[num]
        aux[num]=aux1[:,:]
        lista.append(num)
        lista.append(i)
            




array1=np.hstack((aux[0],aux[1],aux[2],aux[3]))
array2=np.hstack((aux[4],aux[5],aux[6],aux[7]))
array3=np.hstack((aux[8],aux[9],aux[10],aux[11]))
array4=np.hstack((aux[12],aux[13],aux[14],aux[15]))

 
final=np.vstack((array1,array2,array3,array4))    

im=Image.fromarray(final)
im.show()   
    
        
        