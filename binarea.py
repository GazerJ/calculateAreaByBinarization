# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 14:57:44 2021

@author: 94917
"""

from sklearn.cluster import KMeans
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import time
go=time.time()
def getimg():
    return Image.open("./4.jpg")
def showimg(img):
    plt.imshow(img)
    plt.show()
    
im=getimg()
im=np.array(im.convert("RGB"))
r=im[:,:,0]
g=im[:,:,1]
b=im[:,:,2]



ls=(np.sqrt(len(r)**2+len(r[0])**2)/2)
z=np.zeros((len(r),len(r[0])))
for i in range(len(r)):
    for j in range(len(r[0])):
        # 1:20  0.5  244
        #
        z[i,j]=int(b[i,j])#-22*(np.sqrt((i-len(r)/2)**2+(j-len(r[0])/2)**2)/ls)**0.3
        


im=np.where(z<200 ,255,0)


a=np.where(im==0)
print("s="+str(len(a[0])/(len(im)*len(im[0]))))

showimg(Image.fromarray(im))

print(time.time()-go)
'''
for k in range(30):
    for i in range(len(r)):
        for j in range(len(r[0])):
            try:
                #if im[i,j]==0 and (im[i-1,j]+im[i+1,j]+im[i,j+1]+im[i,j-1]+im[i-1,j-1]+im[i+1,j-1]+im[i-1,j+1]+im[i+1,j+1]>255*4):
                #    im[i,j]=255
                if im[i-1,j]==255 and im[i,j]==0 and im[i+1,j]==255:
                    soc=0
                    for l in range(-5,6):
                        for m in range(-5,6):
                            soc+=im[i+l,j+m]
                    if  soc>255*60:#白色占比小于
                        im[i,j]=255
                if im[i,j-1]==255 and im[i,j]==0 and im[i,j+1]==255:
                    soc=0
                    for l in range(-5,6):
                        for m in range(-5,6):
                            soc+=im[i+l,j+m]
                    if  soc>255*60:#白色占比小于
                        im[i,j]=255
                if im[i-1,j-1]==255 and im[i,j]==0 and im[i+1,j+1]==255:
                    soc=0
                    for l in range(-5,6):
                        for m in range(-5,6):
                            soc+=im[i+l,j+m]
                    if  soc>255*60:#白色占比小于
                        im[i,j]=255
            except:
                pass
showimg(Image.fromarray(im))
for k in range(30):
    for i in range(len(r)):
        for j in range(len(r[0])):
            try:
                if im[i-1,j]==0 and im[i,j]==255 :
                    soc=0
                    for l in range(-5,6):
                        for m in range(-5,6):
                            soc+=im[i+l,j+m]
                    if  soc<255*61:#白色占比小于
                        im[i,j]=0
            except:
                pass


a=np.where(im==0)
print("s="+str(len(a[0])/(len(im)*len(im[0]))))

showimg(Image.fromarray(im))

print(time.time()-go)
'''
'''
where=[]
for i in range(len(im[:,0])):
    for j in range(len(im[0,:])):
        if im[i,j]==0:
            where.append([i,j])
'''