# Author: Lindsey Michelle Slagle
# GitHub username: Lswaggerty
# Date: 11/6/2024
# Description: Create a function that takes as a parameter a list and reverses the order of the elements in that list.
def reverse_list(lst):
    """Reverse the order of elements in the list."""
    n = len(lst)
    for i in range(n // 2):
        lst[i], lst[n - i - 1] = lst[n - i - 1], lst[i]
