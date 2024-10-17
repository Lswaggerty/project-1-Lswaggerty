# Author: Lindsey Michelle Slagle
# GitHub username: Lswaggerty
# Date: 10/16/2024
# Description: Asking the program for the minimal value and maximum value of a set of integers.
num_integers = int(input("How many integers would you like to enter?\n"))
print(f"Please enter {num_integers} integers.")
first_num = int(input())
min_num = first_num
max_num = first_num
for _ in range(num_integers - 1):
    current_num = int(input())
    if current_num < min_num:
        min_num = current_num
    if current_num > max_num:
        max_num = current_num
print(f"min: {min_num}")
print(f"max: {max_num}")

