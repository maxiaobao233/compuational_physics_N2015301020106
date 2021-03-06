# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 16:21:27 2017

@author: 马晓宝
"""

from math import *
from pylab import *
x1,y1,x2,y2=[-1.],[0.],[1.],[0.]
vx1,vy1,vx2,vy2=[0.],[-pi],[0.],[pi]
<<<<<<< HEAD
dt=0.001
=======
dt=0.002
>>>>>>> 9740be1280558073ce5ab4d96e9c283e533ab2be
t=[0]
while t[-1]<10:
    r=sqrt((x1[-1]-x2[-1])**2+(y1[-1]-y2[-1])**2)
    vx1.append(vx1[-1]+dt*(-4*pi*pi*(x1[-1]-x2[-1])/(r**3)))
    vy1.append(vy1[-1]+dt*(-4*pi*pi*(y1[-1]-y2[-1])/(r**3)))
<<<<<<< HEAD
=======
    vx2.append(vx2[-1]+dt*(-4*pi*pi*(x2[-1]-x1[-1])/(r**3)))
>>>>>>> 9740be1280558073ce5ab4d96e9c283e533ab2be
    vy2.append(vy2[-1]+dt*(-4*pi*pi*(y2[-1]-y1[-1])/(r**3)))
    x1.append(x1[-1]+vx1[-1]*dt)
    y1.append(y1[-1]+vy1[-1]*dt)
    x2.append(x2[-1]+vx2[-1]*dt)
    y2.append(y2[-1]+vy2[-1]*dt)
    t.append(t[-1]+dt)
figure(figsize=[6,6])
plot(x1,y1,'r')
plot(x2,y2,'b')
xlabel('x')
ylabel('y')
xlim(-0.1,0.1)
ylim(-1.05,-0.98)
title('two stars with same mass')
show()
show()
from visual import *
import os

#my first vpython program!
scene.title='binary star'
scene.forward=vector(0,-0.3,-1)

G=6.7e-11

b=sphere(pos=(-1e11,0,0),color=color.red,radius=4e10, make_trail=True)
b.p=vector(0,0,-1e4)*2e30#p=mv
b.mass=2e30

s=sphere(pos=(1.5e11,0,0),color=color.blue,radius=2e10, make_trail=True)
s.p=-b.p
s.mass=1e30

dt=1e5

counter=0
sshot_iter=0
while True:
    rate(200)
    dist=s.pos-b.pos
    force=G*b.mass*s.mass*dist/pow(mag(dist),3)#gravity,mag means sqrt(x**2+y**2+z**2),pow means power function,pow(x,y)=x**y
    b.p=b.p+force*dt#p=p+F*dt
    s.p=s.p-force*dt
    b.pos=b.pos+b.p/b.mass*dt#pos=pos+v*dt
    s.pos=s.pos+s.p/s.mass*dt

    if counter%10==0:
        os.popen('import -window "binary star" frames/vp'+str(sshot_iter).zfill(4)+'.gif')
        sshot_iter+=1
    counter+=1

