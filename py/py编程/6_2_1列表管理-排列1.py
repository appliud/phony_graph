string = "abedc"
sorted_string = sorted(string)
print(sorted_string)  # 输出：['a', 'b', 'c', 'd', 'e']

#sorted用于对可迭代对象进行排序并返回一个新的已排序的列表
list_1 = [3, 1, 4, 2, 5]
sorted_list = sorted(list_1)
print("list:",list_1) 
print(sorted_list)    # 输出：[1, 2, 3, 4, 5]
print("反向打印列表orted_list")
sorted_list.reverse()
print("sorted_list:",sorted_list)
#reverse() 方法不能直接在 print() 函数中使用
#reverse() 方法是用于修改列表本身的顺序，而不返回一个新的逆序列表
#因此，在 print() 函数中使用 reverse() 方法是无效的，只会返回 None。

#如果想在print()中实现
print("list_1反向",list[::-1])
print("list_1反向",list(reversed(list_1)))#使用list将反向得到的列表创建

tuple = (3, 1, 4, 2, 5)
sorted_tuple = sorted(tuple)
print(sorted_tuple)   # 输出：[1, 2, 3, 4, 5]

dictionary = {'a': 1, 'b': 3, 'c': 2}
sorted_keys = sorted(dictionary.keys())
print(sorted_keys)    # 输出：['a', 'b', 'c']

set = {3, 1, 4, 2, 5}
sorted_set = sorted(set)
print("set:",set)#集合是一种无序的数据结构，因此排序集合时，返回的结果将是一个有序列表，而不是一个集合
print(sorted_set)     # 输出：[1, 2, 3, 4, 5]