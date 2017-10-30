

# Exercise_06
## 题目
（习题3.16）This time I investigate how a strange attractor is altered by small changes irrone of the pendulum parameters.Begin by calculating the strange attractor in Figure 3.9 。Then change either the drive amplitude or drive frequency by a small amount and observe the changes in the attractor.
## 背景
混沌（chaos）是指确定性动力学系统因对初值敏感而表现出的不可预测的、类似随机性的运动。奇怪吸引子又称为混沌吸引子,它具有复杂的拉伸、扭曲的结构.奇怪吸引子是系统总体稳定性和局部不稳定性共同作用的产物,它具有自相似性,具有分形结构.保守系统由于相体积永远不变，所以不存在吸引子，但是耗散系统却存在。对奇异吸引子的研究还处于开始阶段，有无数的形式有待探索和发现。动力学系统的大范围分析被认为是奇异吸引子的数学理论基础，但是关于奇异吸引子的理论还远未完成，所以很有研究空间。
## 常微分方程


![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/61.png)


## 牵引振幅的影响

![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/62.png)


### 1,当牵引力较小时：
做出F_D=0,0.1,0,2^1.1图像如下： 
 F_D=0时： 
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/f_d%3D0.png)
 F_D=0.1时：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/fd%3D0.1.png) F_D=0.2时：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/f-d%3D.png)
 F_D=0.3时：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/fd%3D0.3.png)
 F_D=0.4时：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/fd%3D0_4.png)
 F_D=0.5时：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/fd%3D0.5.png) F_D=0.6时：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/fd%3D0_6.png)
 F_D=0.7时：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/fd%3D0.7.png)
 F_D=0.8时：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/fd%3D0_8.png)
 F_D=0.9时：
![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/fd%3D0.9.png)
 当驱动力较小时，可以看出非线性摆是周期运动。
 ### 2.当驱动力较大时：
 F_D=1.0时：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/fd%3D1_0.png)
 F_D=1.1时： 
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/fd%3D1.1.png)
 F_D=1.2时：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/fd%3D1.2.png)
 当F_D=1.0的时候会开始出现混沌现象，逐渐增加驱动力，混沌现象更加没明显，运动开始有紊乱并且不可预测。
 ### 3,继续增大驱动力
 F_D=1.25时：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/fd%3D1.25.png)
 F_D=1.3时：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/fd%3D1.3.png)
 F_D=1.35时：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/fd%3D1.35.png)
 F_D=1.4时：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/fd%3D1.4.png)
 F_D=1.465时：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/fd%3D1.465.png)
 当驱动力增加到1.25时，混沌现象开始不太明显，继续增加驱动力，在小于1.5的范围内逐渐开始 变得有周期性，混沌现象逐渐消失。
 ### 4，继续增大驱动力
 F_D=1.5时：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/fd%3D1.5.png)
 F_D=1.6时：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/fd%3D1.6.png)
 F_D=1.7时：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/fd%3D1.7.png)
 F_D=1.9时：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/fd%3D1.9.png)
 如果继续增加驱动力，则周期现象又会消失，开始出现混沌现象。
 ## 牵引频率的影响
 
 ![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/63.png)
 
 当Ω_D=1.9： 
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/1.9.png)
 当Ω_D=1.95： 
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/1.95.png)
 当Ω_D=2： 
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/2.png)
 当Ω_D=2.05： 
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/2.05.png)
 当Ω_D=2.1： 
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/2.1.png)
 当Ω_D=2.2： 
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/2.2.png)
 当Ω_D=2.3：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/2.3.png)
 当Ω_D=2.4：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/2.4.png)
 当Ω_D=2.6：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/2.6.png)
 当Ω_D=2.8：
 ![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/2.8.png)
当Ω_D=3.4：
![](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter3/3.4.png)
从模拟图可以看出，很小的驱动频率改变都会对混沌现象造成很大的影响。并且随着驱动频率增加，混沌有逐渐消失的趋势，非线性摆有几乎回归周期性运动的行为。
## 结论
在驱动力或者驱动频率在某一个临界值的时候，非线性摆周期性会突然消失，出现混沌现象，但是随着两者之一有一个逐渐增加的时候，混沌现象会逐渐消失，然后回到周期性运动，但是再增加驱动力或者驱动频率，又会变得混沌不可预测。
## 源程序
[code]()
 
 
 
 
 
 
 
 
 
 
