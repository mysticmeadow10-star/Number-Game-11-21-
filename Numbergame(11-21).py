#Write a program to generate a random integer and match it with the input given by the user?

import random

number =random.randint(1,10)

user = int(input("Guess a value between numbers 1 to 10.:"))

if user == number:
    print("You win! The numbers match ! Hooray")
else:
    print("Try again! The number was",number)