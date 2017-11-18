# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 23:25:55 2017

@author: 马晓宝
"""

import pylab as pl

from math import pi,cos,sin,exp
from scipy import constants
from scipy.constants import g


FD=1.5
T=10000
dt=T/100000
theta=['a']*100001
theta[0]=0.2
w=['a']*100001
w[0]=0
t=['a']*100001
t[0]=0
i=0

while i<100000:
    i0=i+1
    w[i0]=w[i]-(sin(theta[i])+0.5*w[i]-FD*sin((2/3)*t[i]))*dt
    theta[i0]=theta[i]+w[i0]*dt
    t[i0]=t[i]+dt
    if theta[i0]<-pi:
        theta[i0]=theta[i0]+2*pi
    elif theta[i0]>pi:
        theta[i0]=theta[i0]-2*pi
    else:
        theta[i0]=theta[i0]
    i=i+1

    
w_new=['a']*100
theta_new=['a']*100
i=0
while i<100:
    i0=i*100
    w_new[i]=w[i0]
    theta_new[i]=theta[i0]
    i=i+1

w_new2=['a']*100
theta_new2=['a']*100
i=0
while i<100:
    i0=i*942
    w_new2[i]=w[i0]
    theta_new2[i]=theta[i0]
    i=i+1
    

pl.plot(w_new2,theta_new2,'o',markersize=2)
pl.show()
pl.plot(w_new,theta_new,'o',markersize=2)
pl.show()















