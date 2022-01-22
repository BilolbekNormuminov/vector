from vector import Vector

class Point:
    """3d point class"""
    
    def __init__(self, x: float, y: float, z: float) -> None:
        self._x = x
        self._y = y
        self._z = z

    def print(self) -> None:
        print(f"({self._x}, {self._y}, {self._z})")
    
    def transition(self, vector: Vector):
        self._x += vector._i
        self._y += vector._j
        self._z += vector._k

        return self