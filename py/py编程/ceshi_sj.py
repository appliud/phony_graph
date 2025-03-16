from ctypes import *
import time
from numba import jit

@jit
def calc_sum():
    sum_py = 0 
    for i in range(100000000):
        sum_py = sum_py + 1
    print("Python 计算结果：", sum_py)
    return sum_py

start_py = time.time()
result_py = calc_sum()
print("Python 执行时间：", time.time() - start_py)