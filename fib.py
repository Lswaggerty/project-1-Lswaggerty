# Author: Lindsey Michelle Slagle
# GitHub username: Lswaggerty
# Date: 09/30/2024
# Description: Create a function named fib that takes a positive integer parameter and returns the number at that position of the Fibonacci sequence.
def fib(position):
    """
    Calculate the Fibonacci number at the given position in the sequence using a loop.

    Parameters:
    position (int): The position in the Fibonacci sequence (must be a positive integer).

    Returns:
    int: The Fibonacci number at the specified position.
    """
    if position == 1 or position == 2:
        return 1

    # Initializing the first two Fibonacci numbers
    prev1, prev2 = 1, 1

    # Iterating to compute the Fibonacci number at the given position
    for _ in range(3, position + 1):
        fib_number = prev1 + prev2
        prev1, prev2 = prev2, fib_number

    return fib_number
