# Author: Lindsey Michelle Slagle
# GitHub username: Lswaggerty
# Date: 10/30/2024
# Description: create a odometer reading
class Taxicab:
    """
    Represents a Taxicab with x and y coordinates and an odometer to track total distance traveled.
    """

    def __init__(self, x_coord, y_coord):
        """
        Initializes a Taxicab object with initial x and y coordinates and an odometer set to zero.

        Parameters:
        x_coord (int): Initial x-coordinate of the Taxicab.
        y_coord (int): Initial y-coordinate of the Taxicab.
        """
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer = 0

    def get_x_coord(self):
        """
        Returns the current x-coordinate of the Taxicab.

        Returns:
        int: The x-coordinate of the Taxicab.
        """
        return self._x_coord

    def get_y_coord(self):
        """
        Returns the current y-coordinate of the Taxicab.

        Returns:
        int: The y-coordinate of the Taxicab.
        """
        return self._y_coord

    def get_odometer(self):
        """
        Returns the current odometer reading of the Taxicab.

        Returns:
        int: The total distance traveled by the Taxicab.
        """
        return self._odometer

    def move_x(self, distance):
        """
        Moves the Taxicab left or right based on the distance parameter and updates the odometer.

        Parameters:
        distance (int): The distance to move horizontally. Positive for right, negative for left.
        """
        # Update x-coordinate using getter method
        new_x_coord = self.get_x_coord() + distance
        self._x_coord = new_x_coord
        self._odometer += abs(distance)

    def move_y(self, distance):
        """
        Moves the Taxicab up or down based on the distance parameter and updates the odometer.

        Parameters:
        distance (int): The distance to move vertically. Positive for up, negative for down.
        """
        # Update y-coordinate using getter method
        new_y_coord = self.get_y_coord() + distance
        self._y_coord = new_y_coord
        self._odometer += abs(distance)


# Example usage
cab = Taxicab(5, -8)  # Creates a Taxicab object at coordinates (5, -8)
cab.move_x(3)  # Moves cab 3 units "right"
cab.move_y(-4)  # Moves cab 4 units "down"
cab.move_x(-1)  # Moves cab 1 unit "left"
print(cab.get_odometer())  # Prints the current odometer reading; expected output is 8
