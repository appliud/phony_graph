import time

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')  # 或者 'Qt5Agg'

def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    p = 3 - 2 * r
    points = []

    while x <= y:
        points.append((xc + x, yc + y))
        points.append((xc - x, yc + y))
        points.append((xc + x, yc - y))
        points.append((xc - x, yc - y))
        points.append((xc + y, yc + x))
        points.append((xc - y, yc + x))
        points.append((xc + y, yc - x))
        points.append((xc - y, yc - x))

        if p < 0:
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y = y - 1
        x = x + 1

    return points

# 示例调用
xc, yc, r = 0, 0, 10
circle_points = bresenham_circle(xc, yc, r)

# 绘制圆
x_coords, y_coords = zip(*circle_points)
plt.figure()
plt.plot(x_coords, y_coords, 'ro')  # 'ro' 表示红色圆点
plt.title('Bresenham Circle')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.axis('equal')  # 保持 x 和 y 轴比例相同
current_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
plt.savefig('./img/Bresenham_circle'+current_time+'.png')
plt.show()
