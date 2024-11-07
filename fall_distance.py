# Author: Lindsey Michelle Slagle
# GitHub username: Lswaggerty
# Date: 09/30/2024
# Description: Create a function that takes the time in seconds as a parameter. The function should return the distance in meters that the object has fallen in that time.
def fall_distance(time_in_seconds):
    """
    Calculate the distance an object falls due to gravity in a given time period.

    Parameters:
    time_in_seconds (float): The time in seconds the object has been falling.

    Returns:
    float: The distance in meters the object has fallen.
    """
    g = 9.8  # gravitational constant in meters per second squared
    distance = 0.5 * g * (time_in_seconds ** 2)
    return distance
