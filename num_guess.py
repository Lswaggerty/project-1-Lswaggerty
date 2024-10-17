# Author: Lindsey Michelle Slagle
# GitHub username: Lswaggerty
# Date: 10/16/2024
# Description: Asking the program to play a guessing game of numbers by guessing the number and the program prompting if the answer is too high or too low.
target = int(input("Enter the integer for the player to guess.\n"))
num_guesses = 0
correct_guess = False
while not correct_guess:
    guess = int(input("Enter your guess.\n"))
    num_guesses += 1
    if guess > target:
        print("Too high - try again:")
    elif guess < target:
        print("Too low - try again:")
    else:
        correct_guess = True
        if num_guesses == 1:
            print(f"You guessed it in {num_guesses} try.")
        else:
            print(f"You guessed it in {num_guesses} tries.")
