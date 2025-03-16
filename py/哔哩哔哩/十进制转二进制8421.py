b = []#列表
d=11
while True:#True 无限循环
    b = []
    try:
        #print(2**d)
        a = int(input("请输入要转换的数："))
        if((a/1024)>1):
            d=20
        if a == -1:
            break#跳出循环
        elif a >= 0:
            for i in range(d, -1, -1):#从d开始，到-1结束，间隔为-1
                if a >= 2 ** i:
                    a -= 2 ** i
                    b.append(1)
                else:
                    b.append(0)
            print(b)
        else:
            print("请输入非负整数！")
    except ValueError:#与try不符时跳转到他
        print("无效的输入，请重新输入")
