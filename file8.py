import random

num = random.randint(1, 10)
guess = int(input("Guess (1-10): "))

if guess == num:
    print("Correct!")
else:
    print(f"Nope, it was {num}")
