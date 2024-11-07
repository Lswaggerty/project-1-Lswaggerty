# Author: Lindsey Michelle Slagle
# GitHub username: Lswaggerty
# Date: 11/6/2024
# Description: Create a function that takes as a parameter a list of numbers and replaces each value with the square of that value
def square_list(numbers):
    """Replace each value in the list with its square."""
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2
