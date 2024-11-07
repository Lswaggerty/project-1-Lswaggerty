# Author: Lindsey Michelle Slagle
# GitHub username: Lswaggerty
# Date: 10/30/2024
# Description: create a odometer reading
# taxicab.py

class Taxicab:
    """
    Represents a Taxicab with x and y coordinates and an odometer to track total distance traveled.
    """
    def __init__(self, x_coord, y_coord):
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer = 0

    def get_x_coord(self):
        return self._x_coord

    def get_y_coord(self):
        return self._y_coord

    def get_odometer(self):
        return self._odometer

    def move_x(self, distance):
        self._x_coord += distance
        self._odometer += abs(distance)

    def move_y(self, distance):
        self._y_coord += distance
        self._odometer += abs(distance)

# Only run this part if this file is executed directly
if __name__ == "__main__":
    cab = Taxicab(5, -8)
    cab.move_x(3)
    cab.move_y(-4)
    cab.move_x(-1)
    print(cab.get_odometer())  # Expected output: 8

