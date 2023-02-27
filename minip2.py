import random 
top_of_range=input("Type a number: ")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("type number greater than 0")
        quit()
else:
    print("type number next time")
    quit()
random_number=random.randint(0,top_of_range)
guesses=0
while True:
    guesses+=1                                                                       
    user_number=input("guess a number: ")
    if user_number.isdigit():
        user_number=int(user_number)
    if user_number==guesses:
        print("you got it ")
        break
    elif user_number>guesses:
        print("your above the number")
    else:
        print("your below the number")
print("you got it in",guesses,"guesses")