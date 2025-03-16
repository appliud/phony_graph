first_name="ada"
last_name="lovelace"
full_name=f"{first_name,last_name}"#但可以出现数字
print(full_name)
full_name=f"{first_name} 1{last_name,1}"
print(full_name)
print(f"Hello,{full_name.title()}")
message=f"Hello,{full_name.title()}!"#可以创建消息并赋值给变量
print(message)
#print(f"{Hello,full_name.title()}")  {}里不能出现常量
#f字符串，f是format(设置格式的缩写)，把花括号里的变量替换为其值来设置字符串的格式
#非变量部分原样输出
def describe_pet(animal_type,pet_name):
     """显示宠物的信息"""
     print(f"\nI have a {animal_type}.")
     print('\n ',f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
#让实参变成可选的
def get_formatted_name(first_name,last_name,middle_name=''):
     """返回整洁的姓名"""
     if middle_name:
         full_name = f"{first_name} {middle_name} {last_name}"
     else:
         full_name = f"{first_name} {last_name}"
     return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)
musician = get_formatted_name('john','hooker','lee')
print(musician)

#
ceshi1=("小猫猫","小狗狗")
ceshi2="小狗狗"
for i in ceshi1:
    print(f"{i}是我的宠物")