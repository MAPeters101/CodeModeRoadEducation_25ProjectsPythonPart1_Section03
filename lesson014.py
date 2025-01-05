name = input("Enter your name: ")

if name[0].upper() == 'S':
    print("Your name starts with an S!")
else:
    print("Your name does not start with an S.")

import random

num = int(input("Enter a number between 1 an 100: "))
mystery = random.randint(1, 100)

if num > mystery:
    print("Too high!")
elif num < mystery:
    print("Too low!")
else:
    print("You got it!")

print(f"The mystery number is {mystery}")


