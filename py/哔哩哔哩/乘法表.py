def print_multiplication_table():
    num = int(input("请输入一个数字（1-4）来选择打印九九乘法表的方法："))

    if num == 1:
        c=1
        for i in range(1, 10, 1):
            print()
            c = 1+c
            for j in range(1, c, 1):
                print("(%d*%d=%d)" % (i, j, i * j), end='')
    elif num == 2:
        for i in range(1, 10):
            for j in range(1, 10):
                print(f"{i}×{j}={i * j}", end="\t")
            print()
    elif num == 3:
        for i in range(1, 10):
            expression = [f"{i}×{j}={i * j}" for j in range(1, 10)]
            print("\t".join(expression))
    elif num == 4:
        table = [[f"{i}×{j}={i * j}" for j in range(1, 10)] for i in range(1, 10)]
        for row in table:
            print("\t".join(row))
    else:
        print("无效的输入！请重新输入一个数字（1-4）.")


# 调用函数打印九九乘法表
print_multiplication_table()