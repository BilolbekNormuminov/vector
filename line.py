class Line2D:
    """A in x-y plane"""

    def __init__(self, a: int, b: int, c: int) -> None:
        """A line in standard form (ax + by + c = 0)"""

        self._a = a
        self._b = b
        self._c = c