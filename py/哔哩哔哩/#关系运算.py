#关系运算
a=int(input("输入我们队的实力:"))
b=int(input("输入对手1队的实力："))
c=int(input("输入对手2队的实力:"))
d=int(input("输入对手3队的实力:"))

avsb=(a>b)*3+(a==b)

avsc=(a>c)*3+(a==c)

avsd=(a>d)*3+(a==d)

score=avsb+avsc+avsd

print("小组赛球队可以得%d分"%(score))
