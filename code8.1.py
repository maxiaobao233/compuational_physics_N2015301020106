# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:33:59 2017

@author: 马晓宝
"""

import pylab as pl

from math import pi,cos,sin,exp
from scipy import constants
from scipy.constants import g


FD=1.3
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
    w[i0]=w[i]-(sin(theta[i])+0.5*w[i]-FD*sin((pi/5)*t[i]))*dt
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
    i0=i*100+10000
    w_new[i]=w[i0]
    theta_new[i]=theta[i0]
    i=i+1
pl.xlim(-4,4)
pl.ylim(-4,4)


pl.title('FD=1.3')
pl.plot(w_new,theta_new,'ro',markersize=6)
pl.show()


FD=1.6
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
    w[i0]=w[i]-(sin(theta[i])+0.5*w[i]-FD*sin((pi/5)*t[i]))*dt
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
    i0=i*100+10000
    w_new[i]=w[i0]
    theta_new[i]=theta[i0]
    i=i+1
pl.xlim(-4,4)
pl.ylim(-4,4)

pl.title('FD=1.6')

pl.plot(w_new,theta_new,'ro',markersize=6)
pl.show()


FD=1.65
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
    w[i0]=w[i]-(sin(theta[i])+0.5*w[i]-FD*sin((pi/5)*t[i]))*dt
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
    i0=i*100+10000
    w_new[i]=w[i0]
    theta_new[i]=theta[i0]
    i=i+1
pl.xlim(-4,4)
pl.ylim(-4,4)

pl.title('FD=1.65')


pl.plot(w_new,theta_new,'ro',markersize=6)
pl.show()
