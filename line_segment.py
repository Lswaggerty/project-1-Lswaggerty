# Author: Lindsey Michelle Slagle
# GitHub username: Lswaggerty
# Date: 11/26/2024
# Description:Define a Point class that has two data members, _x_coord and _y_coord, representing the two coordinates of the point.

class Point:
    """Represent a point in a 2D space."""

    def __init__(self, x_coord, y_coord):
        """Initialize Point with x and y coordinates."""
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x_coord(self):
        """Return the x-coordinate."""
        return self._x_coord

    def get_y_coord(self):
        """Return the y-coordinate."""
        return self._y_coord

    def distance_to(self, other_point):
        """Return the distance to another Point."""
        dx = self._x_coord - other_point.get_x_coord()
        dy = self._y_coord - other_point.get_y_coord()
        return (dx ** 2 + dy ** 2) ** 0.5


class LineSegment:
    """Represent a line segment defined by two endpoints."""

    def __init__(self, endpoint_1, endpoint_2):
        """Initialize LineSegment with two Point objects as endpoints."""
        self._endpoint_1 = endpoint_1
        self._endpoint_2 = endpoint_2

    def get_endpoint_1(self):
        """Return the first endpoint."""
        return self._endpoint_1

    def get_endpoint_2(self):
        """Return the second endpoint."""
        return self._endpoint_2

    def length(self):
        """Return the length of the LineSegment."""
        return self._endpoint_1.distance_to(self._endpoint_2)

    def slope(self):
        """Return the slope of the LineSegment."""
        x1, y1 = self._endpoint_1.get_x_coord(), self._endpoint_1.get_y_coord()
        x2, y2 = self._endpoint_2.get_x_coord(), self._endpoint_2.get_y_coord()
        if x1 == x2:
            return None
        if y1 == y2:
            return 0
        return (y2 - y1) / (x2 - x1)

    def is_parallel_to(self, other_line_segment):
        """Return True if this LineSegment is parallel to another."""
        if self.length() == 0 or other_line_segment.length() == 0:
            return False
        slope_self = self.slope()
        slope_other = other_line_segment.slope()
        if slope_self is None and slope_other is None:
            return True
        if slope_self is not None and slope_other is not None:
            return abs(slope_self - slope_other) < 0.000001
        return False


