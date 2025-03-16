nostarch_url="http://nostarch.com"
a_1="ht"
print(1,nostarch_url)
print(2,nostarch_url.removeprefix('http://'))#只能删除最前面的
print(3,nostarch_url.removesuffix('.com'))#只能删除最后面的
print(4,'今天天气不错'.removeprefix('今天'))
print(5,'今天天气不错'.lstrip('今天'))#看lstrip
def lstrip(s, chars):#使用循环检查,只要出现就有可能被删除
    chars = set(chars)
    for i in s:
        if i in chars:
            s = s.replace(i, '')#将i替换成空
        else:
            break
    return s
nostarch_url=input()
a_1=input()
print(lstrip(nostarch_url,a_1))
print(set(nostarch_url))#set创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
