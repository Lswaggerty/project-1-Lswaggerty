# Author: Lindsey Michelle Slagle
# GitHub username: Lswaggerty
# Date: 11/6/2024
# Description: Create a function that takes two strings as parameters and returns a Python set containing only those words that appear in both strings.
def words_in_both(str1, str2):
    """Return a set of words that appear in both input strings, case-insensitive."""
    words1 = set(word.lower() for word in str1.split())
    words2 = set(word.lower() for word in str2.split())
    return words1 & words2

