#This Is Number Guessing Game to play with computer

#import required packages
import random

#define a function
def guess(x):
    random_number=random.randint(1,x) #importing number between 1 and x
    guess = 0
    while guess != random_number:
        guess=int(input(f"Guess a number between 1 and {x}:"))
        if guess < random_number:
            print("Your Number is too low!!!")
        elif guess > random_number:
            print("Your numbber is too high!!!")

    print(f"Yahhh!!! You guessed the number {random_number}")

guess(20)#telling function to guess number till 20