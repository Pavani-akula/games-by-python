print("WELLCOME TO MY QUIZ ON COMPUTER BASE")
playing=input("Are you want to play quiz? ")
score=0
if playing.lower() != "yes":
    quit()
print("okay let's play the quiz :) ")

answer=input(" What  cpu stands for? ").lower()
if answer=="central processing unit":
    print("Yeah! it is correct")
    score +=1
else:
    print("oops! it is wrong")
answer=input(" What  ip stands for? ").lower()
if answer=="input":
    print("Yeah! it is correct")
    score +=1
else:
    print("oops! it is wrong")
answer=input(" What is computer language? ")
if answer.lower()=="binary language":
    print("Yeah! it is correct")
    score +=1
else:
    print("oops! it is wrong")
answer=input(" What op stands for? ")
if answer.lower()=="out put":
    print("Yeah! it is correct")
    score +=1
else:
    print("oops! it is wrong")
answer=input(" What  alu stands for? ")
if answer.lower()=="arthematic logical unit":
    print("Yeah! it is correct")
    score +=1
else:
    print("oops! it is wrong")
print("you got"+" " , str(score)  + " ",  "out of five questions")
print("you finish the quiz with"+" ",str(score))