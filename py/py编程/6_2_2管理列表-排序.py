#永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)  # 输出：['audi', 'bmw', 'subaru', 'toyota']

numbers = [10, 6, 8, 4, 2]
numbers.sort(reverse=True)
print(numbers)  # 输出：[10, 8, 6, 4, 2]

# 自定义排序规则，按字符串长度排序
fruits = ['apple', 'banana', 'cherry', 'date']
fruits.sort(key=len)
print(fruits)  # 输出：['date', 'apple', 'cherry', 'banana']
#key 参数在 sort() 方法中用于指定一个函数，用于从列表中的每个元素中提取一个用于比较排序的值。可以理解为根据该函数的返回值进行排序。
#这个函数称为排序键函数，它将应用于列表中的每个元素，并返回用于比较排序的值。根据返回值的大小关系，列表中的元素将按照指定的顺序进行排序。
# 指定逆向排序，按字母顺序降序
fruits = ['orange', 'apple', 'banana', 'grape']
fruits.sort(reverse=True)
print(fruits)  # 输出：['orange', 'grape', 'banana', 'apple']
# 自定义排序键函数，按最后一个字符排序
fruits = ['orange', 'apple', 'banana', 'grape']
fruits.sort(key=lambda x: x[-1])
print(fruits)  # 输出：['apple', 'grape', 'banana', 'orange']