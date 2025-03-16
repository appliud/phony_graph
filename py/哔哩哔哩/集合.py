#创建一个空集合必须使用set();比如a=set()
#打印集合元素时会自动忽略重复的元素；比如此{1，2，1，1，2} 结果为1，2
#a='abcde'//字符串
#b=[1,2,3]//列表
#c=(1,2,'abcde')//元组
#d={'a':1,'b':2,'c':3}//字典
#字典转集合后会将字典中的key添加至集合，value就忽略了//如d转后为{‘a','b','c'}
test = {1, 2, 'abc', 567, 8}
for item in test:  #由于集合是无序的，不能通过索引来访问，使用遍历来访问
    print(item)
nums = {1, 2, 3}  #增加一个元素
nums.add(6)  #移除一个元素
nums.remove(1)
print("\n", nums)
#交集
#取两个集合公共的元素
#&/intersection
#并集
#取两集合的全部元素
#I/union
#差集
#取一个集合中另一个集合没有的元素-/difference
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("a&b为", a & b)
print(a | b)
print(a - b)

num1 = int(input("输入班级1的学生数量："))
class1 = set()  #初始化集合class1
for i in range(0, num1):
    name = input("输入班级1的学生姓名：")
    class1.add(name)

num2 = int(input("输入班级2的学生数量："))
class2 = set()
for i in range(0, num2):
    name = input("输入班级2的学生姓名：")
    class2.add(name)

same = class1 & class2
print("重名的学生：")

for i in same:
    print(i)

print("1班有而2班没的同学：")

for i in class1 - class2:
    print(i)

print("2班有而1班没的同学：")

for i in class2 - class1:
    print(i)
