import time

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')  # 或者 'Qt5Agg'

def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_increment = dx / steps
    y_increment = dy / steps
    x = x1
    y = y1
    x_points = [x]
    y_points = [y]

    for _ in range(steps):
        x += x_increment
        y += y_increment
        x_points.append(round(x))
        y_points.append(round(y))

    return x_points, y_points

# Example usage
x1, y1 = 0, 0
x2, y2 = 100, 100

x_points, y_points = dda_line(x1, y1, x2, y2)

# Plotting the line with matplotlib
plt.figure(figsize=(8, 8))
plt.plot(x_points, y_points, marker='o', linestyle='-') # 绘制折线图
plt.title('DDA Line Drawing Algorithm')# 标题
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)

current_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
plt.savefig('./img/DDA'+current_time+'.png')

plt.show()
