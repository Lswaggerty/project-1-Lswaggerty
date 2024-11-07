# Author: Lindsey Michelle Slagle
# GitHub username: Lswaggerty
# Date: 11/6/2024
# Description: Create a function that a list of first names and only excepts names that start with the letter "K"
def add_surname(names):
    """Return a list of names starting with 'K' with the surname 'Kardashian' added."""
    return [f"{name} Kardashian" for name in names if name.startswith("K")]

