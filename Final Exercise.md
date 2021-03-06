# Final Exercise
## 习题 4.7
### 摘要
本次作业是对二位体系和双星系统的三维形式进行的探索和模拟，并且模拟了太阳系的三维版。
### 问题简介
探索牛顿运动定律等动力学问题是，我们都不能避免摩擦力对我们实验的影响，所以首先我们需要找一个理想的没有摩擦力的实验环境，而太阳系就是一个很好的没有摩擦力的体系，这为我们的实验提供了一个十分理想的实验室，
研究天体问题是一个循序渐进的过程，所以我们不是先直接研究双星系统，而是先从一个太阳和一个行星开始我们问题的研究。
### 理论分析
因为行星运动是一个振荡问题，所以Euler-Cromer方法比Euler方法更好。因为如果使用Euler方法，地球的能量将随时间的推移而变化，但Euler-Cromer方法能够在每个轨道过程中精确地节约能量。所以我们采用Euler—Cromer方法。
考虑一个只有太阳和行星的简单系统，则动态方程可以写作：


![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/f1.png)


我们用太阳和地球之间的平均距离——天文单位AU做单位，用年来计算时间，我们有：


![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/f2.png)


为简单起见，我们把时间取为一年，则：



![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/f3.png)


所以：


![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/f4.png)


对地球有：

![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/f5.png)


如果我们考虑两个没有固定位置的两体问题，就会有八个方程,变量如下：

![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/f6.png)


等式的右边将是：


![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/f7.png)

等等
### 数据分析
首先，我们从最简单的包含一个太阳和一个地球的问题开始，结果如下图:


![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/f8.png)


在遵循基本原则的前提下，我们可以模拟3D太阳系，模拟结果如下：


![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/solar%5B1%5D.gif)


接下来我们让这两个物体具有相同的质量：
注意，我们应该设总动量等于零，初始位置为


![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/f11.png)


初始速度为：


![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/f12.png)


结果如下：


![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/f9.png)


我们将图放大可以看到：


![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/f10.png)


我们可以看到路线几乎是一样的，但是如果我们改变初始条件，结果是完全不同的。 结果会随着初始条件而改变


![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/twobody%5B1%5D.gif)


接下来，我们改变他们的质量，让他们成为双星系统：



![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/output%5B1%5D.gif)



我们让质量较大的为质量较小的的二倍，结果显而易见：较重的星体的半径比较轻的星体的半径小。
### 结论
通过对太阳系的模拟，以此探索两体问题，我们可以得到：
当两个物体具有相同的质量时，它们的轨迹是对称的，当它们具有不同的质量时，质量较大的轨道具有较小的半径；如果其中一个质量非常大时，则半径变为零，变成一个固定的物体。此外，轨迹会随着初始条件的不同而发生变化。
### 源代码
[代码1:太阳与地球模拟](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/f%E2%80%94code1.py)

[代码2：3D太阳系](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/f-code2.py)

[代码3：质量相等的两体问题](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/f-code3.py)

[代码4：3D双星](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/f-code4.py)


