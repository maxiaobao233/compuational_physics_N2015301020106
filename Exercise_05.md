# Exercise_05
姓名：马晓宝  学号：2015301020106
## 背景介绍
本文主要分析投掷棒球时，棒球的自旋对飞行轨迹的轨迹的影响。首先分析忽略棒球的自旋只考虑空气阻力的影响时棒球的轨迹，最后分析加上自旋以后棒球的轨迹有什么变化。
##正文

不考虑自旋 
 不考虑自旋时棒球的轨迹和homework_6中炮弹的轨迹类似，这里就不再重复。


考虑棒球的下旋 
 在考虑棒球的下旋运动后，棒球的运动示意图（这是棒球运动的仰视图）如下所示 
 
 
 
![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/%E6%A3%92%E7%90%83%E2%80%94%E2%80%941.001.jpeg.jpg)



棒球运动的微分方程与homework_6类似，唯一的区别在于多了一个Z方向的受力:



![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/a.png)



棒球运动的微分方程组为： 



![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/b.png)



方程中的参数取值如下：



![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/d.png)



棒球的自旋对轨迹影响的示意图 
 向前初速度取为7m/s，向上初速度取为70m/s时两者的对比图如下所示： 
 
 
 
 ![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/%E5%9B%BE1.png)
 
 
 
 分别做出和图像对比
 
 
 
 ![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/e.png)
 
 
 
 ![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/baseball.x.z.figure_1.png)
 
 
 
 运动参数对比
 
 
 
 ![](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/c.png)
 
 
 
 ## 计算程序：
 [code](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/code8.py)


