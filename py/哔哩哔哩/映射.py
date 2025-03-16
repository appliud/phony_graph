
container={'苹果':'A','桃子':'B','香蕉':'C','梨子':'D'}
print(container)
print(container['桃子'])


price=dict()#dict字典
price['苹果']=5
price['桃子']=6
price['香蕉']=3
price['梨子']=4
#定义水果字典price

print(price)
if '苹果' in price:#判断苹果是否在字典price中
    print("苹果的价格%d"%(price['苹果']))
else: 
    print("该水果不买")

if '荔枝' in price:
    print("荔枝的价格%d"%(price['荔枝']))
else:
    print("该水果不买")

#print(price['荔枝']) 这是个错误因为我们定义的字典里没有他但访问了他

print("今日水果价格：")
for i in price:
    print("%s的价格%d"%(i,price[i]))
print("")

n=int(input("请输入购买水果的种类数量:"))

sum_price=0#总价格

for i in range(0,n):
    fruit=input("请输入购买水果%d的种类："%(i+1))
    num=int(input('输入购买水果%d的数量（斤)'%(i+1)))
    if fruit in price:
        sum_price=sum_price+price[fruit]*num

print("总价格为%d"%(sum_price))

                  