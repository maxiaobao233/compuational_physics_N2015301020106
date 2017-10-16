import matplotlib.pyplot as plt

import math





def area(v_0, theta_0):

    v_x_0 = v_0 * math.cos(theta_0)

    v_y_0 = v_0 * math.sin(theta_0)

    x_0 = 0

    y_0 = 0

    x_i = x_0

    y_i = y_0

    v_x_i = v_x_0

    v_y_i = v_y_0              #初始状态

    

    delta_t = 0.1

    drag_0 = 4 * (10 **(-5))     #drag_0是初始时B_2/m的值

    

    list_x = []

    list_y = []

    list_x.append(x_i)

    list_y.append(y_i)         #利用俩个list记录每0.1秒炮弹位置

    

    while(1):

        drag_i = drag_0 * ((1 - y_i * (6.5 * 10 **(-3)) / 300) ** (2.5))   #a=6.5*10^(-3)K/m, T=300K, α=2.5

        v_i = math.sqrt(v_x_i ** 2 + v_y_i ** 2)

        x_iplus = x_i + v_x_i * delta_t

        y_iplus = y_i + v_y_i * delta_t

        v_x_iplus = v_x_i - drag_i * v_i * v_x_i * delta_t

        v_y_iplus = v_y_i - drag_i * v_i * v_y_i * delta_t - 9.8 * delta_t

        

        if y_iplus < 0:

            x_final = x_i - y_i * ((x_i - x_iplus) / (y_i - y_iplus))

            y_final = 0

            list_x.append(x_final)

            list_y.append(y_final)

            break

        else:

            x_i = x_iplus

            y_i = y_iplus

            v_x_i = v_x_iplus

            v_y_i = v_y_iplus

        

            list_x.append(x_i)

            list_y.append(y_i)

        

    plt.plot(list_x,list_y,label = theta_0 * 180 / math.pi)

    plt.legend()

    plt.title(u"Cannon shell trajectory") # 标题

    plt.xlabel(u"x(m)")

    plt.ylabel(u"y(m)")

    return x_final





area(700,math.pi * 40 / 180)

area(700,math.pi * 30 / 180)

area(700,math.pi * 50 / 180)
