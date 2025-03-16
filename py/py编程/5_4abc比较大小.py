def a_b_c(a, b,c):
    if a>b:
        d=a
    else:
        d=b
    if d>c:
        return d
    else:
        return c
#a,b,c=int(input())
#将输入的字符串按空格分隔后转换为整数
#然后通过 map 函数将其映射为整数类型
a, b, c = map(int, input("请输入三个整数，以空格分隔：").split())
d=a_b_c(a, b, c)
print(d)
