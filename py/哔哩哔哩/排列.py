import matplotlib.pyplot as plt
import random
import time

def one_1():
    #a=int(input())
    a=3

    if a==1:#选择排列
        a_1=[1,-1,3,4,5,6,99,8,9,10,11]
        a1=a_1[-1]
        a2=a_1[0]
        a3=len(a_1)
        i,j=0,0
        for i in range(0,a3,1):
            print("i=",i)
            for j in range(i,a3,1):
                print("j=",j)
                if a_1[i]>a_1[j]:
                    q1=a_1[i]
                    q2=a_1[j]
                    a_1[i]=q2
                    a_1[j]=q1
                #print((i,j),a_1)
        print(a_1)
    if a==2:
        arr = [5, -3, 2, 10, 0, 8]
        n = len(arr)
        for i in range(n-1):  # 执行n-1轮排序
            for j in range(n-1-i):  # 每轮排序需要比较的次数
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]  # 交换位置
    if a==3:
        def bubble_sort_visual(arr):
            n = len(arr)
            fig, ax = plt.subplots()
            ax.set_title('Bubble Sort')
            ax.bar(range(n), arr)
            for i in range(n-1):
                for j in range(n-1-i):
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                        ax.clear()
                        ax.set_title('Bubble Sort')
                        ax.bar(range(n), arr)
                        plt.pause(0.1)  # 暂停一段时间，以便观察排序过程
            plt.show()

            # 测试示例
            arr = [random.randint(1, 100) for _ in range(10)]
            bubble_sort_visual(arr)
   
one_1()
        