# Author: Lindsey Michelle Slagle
# GitHub username: Lswaggerty
# Date: 09/30/2024
# Description: Create a function that takes a positive integer parameter as the initial number of a hailstone sequence and returns how many steps it takes to reach 1
def hailstone(starting_number):
    """
    Calculate the number of steps it takes for a hailstone sequence to reach 1.

    Parameters:
    starting_number (int): The initial positive integer of the hailstone sequence.

    Returns:
    int: The number of steps it takes to reach 1.
    """
    steps = 0  # Initialize step counter

    # If starting number is already 1, return 0 steps
    if starting_number == 1:
        return steps

    # Continue the hailstone sequence until we reach 1
    while starting_number != 1:
        if starting_number % 2 == 0:
            starting_number //= 2  # If even, divide by 2
        else:
            starting_number = starting_number * 3 + 1  # If odd, multiply by 3 and add 1
        steps += 1  # Increment the step counter for each operation

    return steps
