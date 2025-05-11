import numpy as np

number = np.random.randint(1, 101)

count = 0
while True:
    guess = input("Guess a number between 1 and 100: ")
    count += 1
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {count} tries.")
        break