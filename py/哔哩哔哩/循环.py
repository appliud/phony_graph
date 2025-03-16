#for i in range(0,10):#最后是冒号（：），从0到n-1
#    print("i=%d"%(i))
print("兔子翻倍\n问题")#\n换行
rabbit=3
print("请输入N的值:")
N=int(input())
for i in range(0,N):
    rabbit=rabbit*2
print("%d年后,兔子的数量为%d"%(N,rabbit))
print("前n项和")
print("请输入n的值：")
n=int(input())
for a in range(0,n):
    n=n+a
print("n=%d"%n)