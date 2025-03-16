players=['charles','martina','michael','florence','eli']
print("players:\n",players)
print("players[0:3]:\n",players[0:3])
print("players[1:4]:\n",players[1:4])
print("players[:4]:\n",players[:4])
print("players[2:]:\n",players[2:])
print("players[-3:]:\n",players[-3:])
print("players[:-1]:\n",players[:-1])

for player in players[:3]:
    print(player.title())

my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
print("my_foods:\n",my_foods)
print("friend_foods:\n",friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("my_foods:\n",my_foods)
print("friend_foods:\n",friend_foods)
