# Practical 14: Inherit 2DPoint to create 3DPoint
import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    # Override distance() to include the z-coordinate.
    def distance(self, other):
        return math.sqrt(
            (other.x - self.x) ** 2
            + (other.y - self.y) ** 2
            + (other.z - self.z) ** 2
        )


x1 = float(input("Enter x, y and z of first point: "))
y1 = float(input("Enter y-coordinate of first point: "))
z1 = float(input("Enter z-coordinate of first point: "))

x2 = float(input("Enter x-coordinate of second point: "))
y2 = float(input("Enter y-coordinate of second point: "))
z2 = float(input("Enter z-coordinate of second point: "))

point1 = Point3D(x1, y1, z1)
point2 = Point3D(x2, y2, z2)

print("Distance between 3D points:", point1.distance(point2))
