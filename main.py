from vector import Vector
from point import Point


def main() -> None:
    my_vector1 = Vector(-1, 5, 0)
    my_vector2 = Vector(3, 2, 8)

    my_point1 = Point(2, 3, 5)

    my_point1.transition(my_vector1).print()

if __name__ == "__main__":
    main()
