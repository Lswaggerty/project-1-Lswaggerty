# Author: Lindsey Michelle Slagle
# GitHub username: Lswaggerty
# Date: 11/6/2024
# Description: Create a function that takes a list of numbers and returns with the median of the list of numbers
def find_median():
    """Return the statistical median of a predefined list of numbers."""
    numbers = [13, 7, -3, 82, 4]  # predefined list of values
    if not numbers:
        return None
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid1, mid2 = sorted_numbers[(n // 2) - 1], sorted_numbers[n // 2]
        return (mid1 + mid2) / 2

# Example usage
result = find_median()  # result should be 7
print("Median:", result)


