for i in range(1,10+1):
    print(i)
number=list(range(1,10+1))#list列表
print("min=",min(number))#最小
print("max=",max(number))#最大
print("sum=",sum(number))#求和

print("number=",number)
number_1=list(range(1,10+1,2))#list列表
print("number_1=",number_1)
squares=[]

for value in range(1,10+1):
    square=value**2#平方
    squares.append(square)#append()追加在最后
print("squares=",squares)

#列表推导式
squares_1=[value**2 for value in range(1,10+1)]
print("squares_1=",squares_1)

import time
start_time = time.time()
count = 0
for i in range(1, 1000000+1):
    print(i, end=" ")
    count += 1
    if count % 5 == 0:
        print()
end_time = time.time()
execution_time = end_time - start_time
print("代码执行时间为:", execution_time, "秒")

add=list(range(1,1000000+1))
print(sum(add))