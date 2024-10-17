# Author: Lindsey Michelle Slagle
# GitHub username: Lswaggerty
# Date: 10/16/2024
# Description: Asking the program for the factors of a given integer.
num = int(input("Please enter a positive integer: "))
print(f"The factors of {num} are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
