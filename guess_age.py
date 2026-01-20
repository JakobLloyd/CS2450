import random

print("Hello! I am going to try to guess your age.")

name = input("What is your name? ")

while True:
    age = random.randint(15, 30)
    answer = input(f"Is your age {age}? (y/n): ")

    if answer == 'y':
        print(f"{name} is {age} years old.")
        break
    else:
        print("Rats.")
