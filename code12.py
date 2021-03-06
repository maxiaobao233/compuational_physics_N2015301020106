# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 11:33:28 2017

@author: 马晓宝
"""


import pylab as pl
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#定义矩阵部分
V1=1
V2=-1
n=30
x1=11#两电容器水平位置，限制列
x2=20
y1=11#两电容器竖直位置，限制行
y2=20
v1=np.zeros((n,n))
for m in range(y1-1,y2+0):#需要控制的列为6-15，在范围处修正
    v1[m][x1-1]=V1
    v1[m][x2-1]=V2
else:
    v1=v1


#计算部分
i1=2
j1=2
sum=np.sum(v1)
SUM=[sum]
deta=1
DETA=[]


while deta>10**(-6):

    while i1<=n-1:
        while j1<=n-1:#此时代表真实行列
           i=i1-1   #排序修正
           j=j1-1
           if j==x1 and y1<=i<=y2:
               v1[i][j]=V1
               j1=j1+1
           elif j==x2 and y1<=i<=y2:
               v1[i][j]=V2 #除去中间边界
               j1=j1+1
           else:
              b=(v1[i-1][j]+v1[i+1][j]+v1[i][j+1]+v1[i][j-1])/4
              v1[i][j]=b
              j1=j1+1
        else:
            i1=i1+1
            j1=2
    else:
       sum=np.sum(v1)
       SUM.append(sum)
       deta=SUM[-1]-SUM[-2]
       DETA.append(deta)
       i1=2
       j1=2
       

else:
    print("over")




#作图模块
fig = pl.figure(figsize=(12,10))
ax = Axes3D(fig)
x = np.linspace(-1, 1,n)
y = np.linspace(-1, 1,n)
x, y = np.meshgrid(x, y)

pl.xlabel("x",size=15)
pl.ylabel("y",size=15)
ax.set_zlabel("potential/V",size=15)
pl.title("Potential of Capacitor",size=17)
ax.set_zlim(-1,1)
ax=pl.subplot(111,projection='3d')
ax.plot_surface(x, y, v1, rstride=1, cstride=1, cmap='rainbow')
pl.show()
