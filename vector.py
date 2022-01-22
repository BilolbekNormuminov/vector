class Vector:
    """A 3d vector class"""

    def __init__(self, i: float = 0, j: float = 0, k: float = 0) -> None:
        self._i = i
        self._j = j
        self._k = k

    def print(self) -> None:
        """Print vector in format <x>i + <y>j + <z>k"""

        components = {
            "i": self._i,
            "j": self._j,
            "k": self._k
        }

        for component in components:
            if components[component]:
                print("{magnitude:+}{direction} ".format(magnitude=components[component], direction=component), end="")

        print()
