import random
player = None
computer = None
running = True
options =("x","o","no")
while running:
    player = input('請輸入剪刀石頭布')
    while player not in options:
      print("請輸入剪刀石頭布")
computer = random.choice(options)
print(f"player:{player}  computer:{computer}")
if player == computer:
    print("平手")
elif player =="x"  and computer == "no":
    print("電腦輸了")
elif player == "o" and computer == "x":
    print("電腦輸了")
elif player == "no" and computer == "o":
    print("電腦輸了")
else:
    print("你輸了")
