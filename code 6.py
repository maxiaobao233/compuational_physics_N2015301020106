import math
def area(v_0, theta_0):
    v_x_0 = v_0 * math.cos(theta_0)
    v_y_0 = v_0 * math.sin(theta_0)
    x_0 = 0
    y_0 = 0
    x_i = x_0
    y_i = y_0
    v_x_i = v_x_0
    v_y_i = v_y_0             
    delta_t = 0.1
    drag_0 = 4 * (10 **(-5))     
    list_x = []
    list_y = []
    list_x.append(x_i)
    list_y.append(y_i)        
    while(1):
        drag_i = drag_0 * ((1 - y_i * (6.5 * 10 **(-3)) / 300) ** (2.5))   #a=6.5*10^(-3)K/m, T=300K, α=2.5
        v_i = math.sqrt(v_x_i ** 2 + v_y_i ** 2)
        x_iplus = x_i + v_x_i * delta_t
        y_iplus = y_i + v_y_i * delta_t
        v_x_iplus = v_x_i - drag_i * v_i * v_x_i * delta_t
        v_y_iplus = v_y_i - drag_i * v_i * v_y_i * delta_t - 9.8 * delta_t
        if y_iplus < 0
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
     return x_final
area_max = area(700,math.pi * 30 / 180)
for i in range(21):
    n = i + 30
    area_2 = area(700,math.pi * n / 180)
    if area_max >= area_2:
        max_angle = 30
    else:
        area_max = area_2
        max_angle = n
print("when the range is maximun of %d m"%(area_max))
print("the angle is %d"%(max_angle))