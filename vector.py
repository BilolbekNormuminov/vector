from math import sqrt, acos


class Vector:
    """A 3d vector class"""

    def __init__(self, i: float = 0, j: float = 0, k: float = 0) -> None:
        self._i = i
        self._j = j
        self._k = k

    def __add__(self, other):
        self._i += other._i
        self._j += other._j
        self._k += other._k

        return self
    
    def __sub__(self, other):
        self._i -= other._i
        self._j -= other._j
        self._k -= other._k

        return self

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            self._i *= other
            self._j *= other
            self._k *= other

            return self
        elif type(other) is Vector:
            return self._i * other._i + self._j * other._j + self._k * other._k
        else:
            raise TypeError

    def to_str(self) -> str:
        """Print vector in format <x>i + <y>j + <z>k"""

        components = {
            "i": self._i,
            "j": self._j,
            "k": self._k
        }

        s = ""

        for component in components:
            if components[component]:
                s += "{magnitude:+}{direction} ".format(magnitude=components[component], direction=component)

        return s
    
    def magnitude(self) -> float:
        return sqrt(pow(self._i, 2) + pow(self._j, 2) + pow(self._k, 2))

    def unit_vector(self):
        return self * (1/self.magnitude())
    
    def is_parallel(self, other) -> bool:
        return True if (self._i / other._i) == (self._j / other._j) == (self._k / other._k) else False

    def is_equal(self, other) -> bool:
        return True if self._i == other._i and self._j == other._j and self._k == other._k else False

    def is_perpendicular(self, other) -> bool:
        return True if self * other == 0 else False
    


def angle(vector1: Vector, vector2: Vector) -> float:
    return acos((vector1 * vector2) / (vector1.magnitude() * vector2.magnitude()))

class Line:
    """A line represented in vector equation form: a + t(b). Where a and a vectors"""

    def __init__(self, point: Vector, direction: Vector) -> None:
        self._point = point
        self._direction = direction

    def to_str(self) -> str:
        return f"{self._point.to_str()} + t({self._direction.to_str()})"
    