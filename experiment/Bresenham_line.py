import time

import matplotlib
from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator
matplotlib.use('TkAgg')  # 或者 'Qt5Agg'

def line(x0, y0, x1, y1):
    x = []
    y = []
    steep = abs(y1 - y0) > abs(x1 - x0)
    if steep:  # 如果为真，说明斜率绝对值大于1，则主要以y方向递增
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    if x0 > x1:  # 如果为真，说明起点大于终点，此时则交换方向
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    delta_x = x1 - x0
    delta_y = abs(y1 - y0)
    error = 0
    delta_error = delta_y / delta_x
    yk = y0

    if y0 < y1:
        y_step = 1
    else:
        y_step = -1

    for xk in range(x0, x1):
        if steep:
            x.append(yk)
            y.append(xk)
        else:
            x.append(xk)
            y.append(yk)

        error = error + delta_error
        if error >= 0.5:
            yk = yk + y_step
            error = error - 1.0
    return x, y


if __name__ == '__main__':
    x, y = line(30, 30, 4, -20)

    plt.xlim((-10, 30))
    plt.ylim((-10, 30))
    plt.grid()
    plt.plot(x, y)

    y_major_locator = MultipleLocator(1)
    x_major_locator = MultipleLocator(1)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    ax.yaxis.set_major_locator(y_major_locator)

    current_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    plt.savefig('./img/Bresenham_line' + current_time + '.png')

    plt.show()
