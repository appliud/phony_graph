#列表是一种有序、可变且允许重复元素的数据结构。列表用方括号[]表示，并且元素之间使用逗号分隔。
bicycles=["trek", "cannondale", "redline", "specialized"]
print(bicycles)
a=0
print(bicycles[a])#[0]列表的索引,可以是变量
print(bicycles[1].title())#首字母大写
print(bicycles[-1])#python提供的特殊方法，使用-1直接访问最后一个元素，-2，-3都可以
message=f"My first bicycles was a {bicycles[0].title()}."
print(message)