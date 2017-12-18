# Exercise_11
## 习题6.6
### 概述
线性方程的一个重要特征是两个解的和也是一个解。这样做的一个后果是，波包将彼此独立运行。一种特别清晰的方法是，用初始配置文件设置一个字符串，这样就有两个高斯波包，位于字符串的不同位置。这些波包(或元件)可能会相互传播并碰撞。显示两个这样的波包通过彼此而不改变形状或速度。
### 引言
波通常被直观地理解为指一种空间扰动的传输，而这种空间扰动通常不伴随着媒质占据整个空间的运动。在波中，振动的能量以扰动的形式从源中移动到周围介质中。然而，这种运动对于驻波来说是有问题的，能量在两个方向上都是相同的，或者是在真空中的电磁波，介质的概念不适用，与目标的相互作用是波探测和实际应用的关键。海面上有水波;太阳发射的伽玛波和光波;微波用于微波炉和雷达设备;无线电台广播;由无线电接收器、电话和生物(如声音)产生的声波，只提到了一些波动现象。
### 方法步骤
波运动的基本方程为：


![](https://github.com/yyx1996/computational_physics_N2015301020105/raw/master/pic12-1.png)


将从相邻的线段上得到的力，i + 1(和i -1)这些力的垂直分量将等于弦T的张力，乘以sin()这里是弦与水平方向的夹角。如果我们假设弦的位移是小的，那么，角度theta_i也是小的，我们可以写出i段的运动方程


![](https://github.com/yyx1996/computational_physics_N2015301020105/raw/master/pic12-2.png)


为了方便设计程序计算，我们将其写成下面的形式：


![](https://github.com/yyx1996/computational_physics_N2015301020105/raw/master/pic12-3.png)


### 结果
l=1m, x=0.6m, k=1500


![](https://github.com/yyx1996/computational_physics_N2015301020105/raw/master/pic12-4.png)


在弦上施加两个干扰


![](https://github.com/yyx1996/computational_physics_N2015301020105/raw/master/pic12-5.png)

![](https://github.com/yyx1996/computational_physics_N2015301020105/raw/master/pic12-6.png)

### 结论
由两个扰动引起的波可以相互独立传播。波的形状和速度等性质在它们加入到一起之前和之后都是一样的。它们满足线性叠加原理。
### 代码
[souce code](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/code13.py)
