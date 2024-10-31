# Author: Lindsey Michelle Slagle
# GitHub username: Lswaggerty
# Date: 10/30/2024
# Description: Create a recursive function that takes two positive integers as parameters and returns the product of those two numbers
def multiply(multiplier, multiplicand):
    """
    Recursively calculates the product of two positive integers using addition.

    Parameters:
    multiplier (int): The number to be multiplied.
    multiplicand (int): The number of times to add the multiplier.

    Returns:
    int: The product of multiplier and multiplicand.
    """
    # Base case: if multiplicand is 1, return the multiplier
    if multiplicand == 1:
        return multiplier

    # Recursive case: add multiplier to the result of multiplying by (multiplicand - 1)
    return multiplier + multiply(multiplier, multiplicand - 1)

# Running a sample multiplication without user input
result = multiply(7, 4)  # This should calculate 7 * 4
print(result)  # Expected output: 28



