import time

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')  # 或者 'Qt5Agg'
def decode_directions(start_x, start_y, directions):
    x, y = start_x, start_y
    path = [(x, y)]
    direction_map = {
        0: (1, 0),   # 向右 (E)
        1: (1, 1),   # 右上 (NE)
        2: (0, 1),   # 向上 (N)
        3: (-1, 1),  # 左上 (NW)
        4: (-1, 0),  # 向左 (W)
        5: (-1, -1), # 左下 (SW)
        6: (0, -1),  # 向下 (S)
        7: (1, -1)   # 右下 (SE)
    }

    for direction in directions:
        dx, dy = direction_map[direction]
        x += dx
        y += dy
        path.append((x, y))

    return path

# 定义起始点和方向编码
start_x, start_y = 0, 0
directions = [0, 0, 0, 0, 1, 2, 3, 4, 4, 4, 0, 0, 0, 1, 2, 3, 4, 4, 4, 4, 0, 6, 6, 6, 6, 6, 6]

# 解码方向编码
path = decode_directions(start_x, start_y, directions)

# 提取路径的 x 和 y 坐标
x_coords, y_coords = zip(*path)

# 绘制路径并添加箭头
plt.figure(figsize=(8, 8))
plt.plot(x_coords, y_coords, 'ro-', label='Path')
plt.plot(x_coords[0], y_coords[0], 'go', label='Start')  # 起点
plt.plot(x_coords[-1], y_coords[-1], 'bo', label='End')  # 终点

# 添加箭头
for i in range(len(path) - 1):
    plt.quiver(x_coords[i], y_coords[i], x_coords[i + 1] - x_coords[i], y_coords[i + 1] - y_coords[i],
               angles='xy', scale_units='xy', scale=1, color='blue')

plt.title('B Shape with Arrows')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.axis('equal')
plt.legend(loc='upper left')
current_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
plt.savefig('./img/方向编码式字符'+current_time+'.png')
plt.show()