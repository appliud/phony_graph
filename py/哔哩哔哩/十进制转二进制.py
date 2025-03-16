def decimal_to_binary(decimal_num):
    #decimal_num在没有声明时为任意类型
    #print("2",type(decimal_num))
    binary_num = ""
    #print("3",type(decimal_num))
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        #将rastructure通过str拼接在binary_num前面
        #binary_num = binary_num + str(remainder)是拼接在后面
        print(binary_num)
        decimal_num = decimal_num // 2
    #print("4",type(decimal_num))
    return binary_num

# 示例：将十进制数13转换为二进制数
decimal = 13
binary = decimal_to_binary(decimal)
#print("1",type(binary))
print("十进制数", decimal, "对应的二进制数为", binary)