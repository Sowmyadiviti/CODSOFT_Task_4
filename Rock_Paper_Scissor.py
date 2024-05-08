import random
print("Welcome to ROCK,PAPER,SCISSORS Game")
print("\n")
print("Winning rules are as under:\nRock vs scissors hence Rock wins \npaper vs Rock hence paper wins \nscissors vs paper hence scissors wins")
print("\n")
list_=["ROCK","PAPER","SCISSORS"]
user=input("Choose one:'ROCK','PAPER','SCISSORS':")
print("Choice you chosen:",user)
computer=random.choice(list_)
print("Random choice by computer:",computer)
if user=="ROCK" and computer=="SCISSORS":
    print("HEY YOU WON!!!")
elif user=="PAPER" and computer=="ROCK":
    print("HEY YOU WON!!!")
elif user=="SCISSORS" and computer=="PAPER":
    print("HEY YOU WON!!!")
elif user==computer:
    print("It is a Tie")
else:
    print("YOU FAILED!!!")
