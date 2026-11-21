# Practical 13: Define a 2DPoint class and calculate distance
import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(f"({self.x}, {self.y})")

    def distance(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)


x1 = float(input("Enter x-coordinate of first point: "))
y1 = float(input("Enter y-coordinate of first point: "))
x2 = float(input("Enter x-coordinate of second point: "))
y2 = float(input("Enter y-coordinate of second point: "))

point1 = Point2D(x1, y1)
point2 = Point2D(x2, y2)

print("First point:", end=" ")
point1.display()
print("Second point:", end=" ")
point2.display()
print("Distance:", point1.distance(point2))
