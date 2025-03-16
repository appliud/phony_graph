import time
def a_1(a,b):#位数
    for i in range(b,-1,-1):
        #print(i)
        if(a>=(10**i)and a<(10**(i+1))):
            print("第",i+1,"位")
            return i+1
            break

def a_2(a,b):#反向
    c=[]
    print("i是当前位数")
    for i in range(b,0,-1):
        print("i",i)
        d=int(a/(10**(i-1)))#得到每一位
        a=int(a)-d*(10**(i-1))
        c.insert(0,d)#添加到最前面
    print(c) 
    c=[str(item) for item in c]#将列表中的元素转换位字符   
    e=''.join(c)#将列表c的内容转位字符
    print("最终结果",e)
    
    
a=int(input())#输入
b=10
if(a<10**5):
    b=5
c=a_1(a,b)
a_2(a,c)

#time.sleep(6)  # 程序将会暂停 1 秒钟
from tqdm import tqdm
for i in tqdm(range(10)):#100*0.1=10s
    time.sleep(0.1)