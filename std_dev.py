# Author: Lindsey Michelle Slagle
# GitHub username: Lswaggerty
# Date: 11/6/2024
# Description: Create a function that defines a class and a different function that takes as a parameter a list of Person objects and returns the standard deviation of all their ages
class Person:
    """Represent a person with a name and age."""

    def __init__(self, name, age):
        """Initialize the name and age of the person."""
        self._name = name
        self._age = age

    def get_age(self):
        """Return the age of the person."""
        return self._age


def std_dev(person_list):
    """Return the population standard deviation of ages in a list of Person objects."""
    if not person_list:
        return None
    ages = [person.get_age() for person in person_list]
    mean_age = sum(ages) / len(ages)
    variance = sum((age - mean_age) ** 2 for age in ages) / len(ages)
    return variance ** 0.5


