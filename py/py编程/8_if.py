cars=['audi','bmw','benz']
for car in cars:
    if car=='bmw':
        print('bmw')
    else:
        print(car)

car='bmw'
print("bmw",car=='bmw')
car='Bmw'
print("Bmw",car=='bmw')
print("Bmw",car.title()=='Bmw')#忽略大小写
print("Bmw",car.lower()=='bmw')#忽略大小写
print("Bmw",car.upper()=='BMW')#忽略大小写

requested_topping='mushrooms'
#不等   
if requested_topping!='anchovies':
    print("Hold the anchovies!")

answer=17
if answer!=42:
    print("That is not the correct answer. Please try again!")

banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
    print(user.title()+", you can post a response if you wish.")

age=19
if age>=18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#elif
age=12
if age<4:
    print("Your admission cost is .")
elif age<18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $00.")

price=0
if age<4:
    price=0
elif age<18:
    price=5
else:
    price=10
print(f"Your admission cost is ${price}.")

#省略else
age=19
if age<4:
    price=0
elif age<18:
    price=5
elif age<65:
    price=10
else:
    price=5
print(f"Your admission cost is ${price}.")

requested_toppings=['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!\n")

requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!\n")

requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping=='green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")