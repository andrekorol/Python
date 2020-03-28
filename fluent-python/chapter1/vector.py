from functools import total_ordering
from math import hypot


@total_ordering
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def _is_valid_operand(self, other):
        return (hasattr(other, 'x')) and (hasattr(other, 'y'))

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return abs(self) < abs(other)
