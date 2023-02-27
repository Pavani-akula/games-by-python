import random
user_wins=0
computer_wins=0
options=["rock","paper","scissor"]
while True:
    user_pick=input("rock/paper/scissor or q to quit ").lower()
    if user_pick=="q":
        break
    if user_pick  not in options:
        continue
    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print("computer picked",(computer_pick), ".")
    if user_pick=="rock"and computer_pick=="scissor":
        print("you won it")
        user_wins=+1
    elif user_pick=="paper" and computer_pick=="rock":
        print("you won it")
        user_wins=+1
    elif user_pick=="scissor" and computer_pick=="paper":
        print("you won it")
        user_wins=+1
    else:
        print("computer won it")
        computer_wins=+1
print("you won it in",user_wins,"times")
print("computer won it in",computer_wins,"times")
print("GoodBye")