# Number Guessing Game
import random

lowest_num = 0
highest_num = 100
guesses = 0
answer = random.randint(lowest_num, highest_num)

print("Welcome to Python Number Guessing Game")

while True:

    guess = input(f"Guess a number between {lowest_num} and {highest_num}: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("Invalid Number")
            print(f"Enter a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too Low! , Try Again")
        elif guess > answer:
            print("Too High!, Try Again")
        else:
            print(f"Correct! , The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            break

    else:
        print("Invalid Number")
        print(f"Enter a number between {lowest_num} and {highest_num}")