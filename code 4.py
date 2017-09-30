T=input('T=')
T=float(T)
delta_t=T/100
t=['a']*101
x=['a']*101
x[0]=0
t[0]=0
i=0
while i<100:
    i0=i+1
    x[i0]=x[i]+40*delta_t
    t[i0]=t[i]+delta_t
    i=i+1
import pylab as pl
import numpy as np
t1=np.arange(0,t[100],0.1)
x1=40*t1
pl.plot(t1,x1,'b')
5pl.plot(t,x,'r')
pl.xlim(0,t[100])
pl.ylim(0,x[100])
pl.xlabel('t')
pl.ylabel('x')
pl.title('displacement changed t')
pl.show()
    