# Exercise_03
## Background:
The position of an object moving horizontally with a constant velocity, v, is described by the equation 

![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/12.png)

Assuming that the velocity is a constant, say , use the Euler method to solve (1.9) for  as a function of time. Compare your result with the exact solution.
## Numberical Approach:
According to the question, we can get :
![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/1.jpg)


According to Taylor Formula:
![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/2.jpg)

put  it into (1.9):
## Source code:
for the specific code
[Source code](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/code%204.py)
## Result analysis and conclusion:
![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/0_D1B9~_1(XY4%5B7W6)%5DHYSB.png)


From the result, we can get that the x is proportional to time t.And the analytical result is


![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/3.png)


Bring the initial condition x=0  and t=0 into (1) 
 We can get  C=0
 So we can get ananlytical result
 
 
![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/4.png)
 
 
 We will find it match with the figure greatly! And the result we get from the Euler method is equal to the analytical result.
