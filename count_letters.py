# Author: Lindsey Michelle Slagle
# GitHub username: Lswaggerty
# Date: 11/6/2024
# Description: Create a function that takes as a parameter a string and returns a dictionary that tabulates how many of each letter is in that string.
def count_letters(s):
    """Return a dictionary counting each letter in the string, case-insensitive."""
    letter_counts = {}
    for char in s:
        upper_char = char.upper()
        if 'A' <= upper_char <= 'Z':
            if upper_char in letter_counts:
                letter_counts[upper_char] += 1
            else:
                letter_counts[upper_char] = 1
    return letter_counts
