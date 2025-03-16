def a_1():
    print(motorcycles)
motorcycles=['honda', 'yamaha', 'suzuki','motor','asddawd']
del motorcycles[0]#删除列表指定位置的元素，不能再使用
a_1()
popped_motorcycles=motorcycles.pop()#删除列表末尾元素，并还能接着使用它
a_1()
print(popped_motorcycles)
popped_motorcycles=motorcycles.pop(1)#也可以删除列表中指定位置的元素
print(popped_motorcycles)
motorcycles=['honda', 'yamaha', 'suzuki','motor','asddawd']
motorcycles.remove('honda')#通过元素的值删除，可以继续使用
#只能删除第一次出现的指定的值，如何该值在列表中多次出现者需要循环
a_1()