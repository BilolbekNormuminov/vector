from math import degrees, radians
from vector import Vector, angle


def main() -> None:
    my_vector1 = Vector(2, -1, -1)
    my_vector2 = Vector(1, -2, 4)
    
    print(degrees(angle(my_vector1, my_vector2)))
    print(my_vector1.is_perpendicular(my_vector2))


if __name__ == "__main__":
    main()
