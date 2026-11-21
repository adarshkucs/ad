# Practical 1: Find the roots of a quadratic equation
 

import cmath


a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))


if a == 0:

    print("This is not a quadratic equation because a cannot be 0.")
else:
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    print("First root:", root1)
    print("Second root:", root2)

# Practical 2: Check prime, generate primes up to n, and first n primes
def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

n = int(input("Enter a number n: "))

print(n, "is prime." if is_prime(n) else "is not prime.")

print("Prime numbers up to", n, ":")
for value in range(2, n + 1):
    if is_prime(value):
        print(value, end=" ")
print()

first_n = []
candidate = 2
while len(first_n) < n:
    if is_prime(candidate):
        first_n.append(candidate)
    candidate += 1

print("First", n, "prime numbers:", first_n)


# Practical 3: Print a star pyramid and a reverse star pyramid
rows = int(input("Enter the number of rows: "))

print("Star pyramid:")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

print("Reverse star pyramid:")
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "* " * i)


# Practical 4: Identify and analyse a character
digit_names = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
               "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

character = input("Enter one character: ")

if len(character) != 1:
    print("Please enter exactly one character.")
elif character.isalpha():
    print("The character is a letter.")
    if character.isupper():
        print("It is an uppercase letter.")
    else:
        print("It is a lowercase letter.")
elif character.isdigit():
    print("The character is a numeric digit.")
    print("Digit in words:", digit_names[int(character)])
else:
    print("The character is a special character.")

# Practical 5: Perform operations on a string
text = input("Enter a string: ")
character = input("Enter the character to search/remove: ")

print("Frequency:", text.count(character))

old_char = input("Enter the character to replace: ")
new_char = input("Enter the new character: ")
print("After replacement:", text.replace(old_char, new_char))

print("After removing first occurrence:", text.replace(character, "", 1))
print("After removing all occurrences:", text.replace(character, ""))


# Practical 6: Swap the first n characters of two strings
first = input("Enter the first string: ")
second = input("Enter the second string: ")
n = int(input("Enter n: "))

if n < 0 or n > len(first) or n > len(second):
    print("Invalid n. It must not exceed the length of either string.")
else:
    swapped_first = second[:n] + first[n:]
    swapped_second = first[:n] + second[n:]
    print("First string after swapping:", swapped_first)
    print("Second string after swapping:", swapped_second)

    

# Practical 7: Find all starting indices of the second string in the first
def find_occurrences(first_string, second_string):
    if second_string == "":
        return -1

    indices = []
    start = 0
    while True:
        index = first_string.find(second_string, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1  # Also finds overlapping occurrences.

    return indices if indices else -1


first = input("Enter the first string: ")
second = input("Enter the second string: ")
print("Indices:", find_occurrences(first, second))

# Practical 8: Cubes of even integers in an input list
items = input("Enter list elements separated by spaces: ").split()

numbers = []
for item in items:
    try:
        numbers.append(int(item))
    except ValueError:
        pass  # Ignore elements that are not integers.

# Method 1: Using a for loop
cubes_for_loop = []
for number in numbers:
    if number % 2 == 0:
        cubes_for_loop.append(number ** 3)

# Method 2: Using list comprehension
cubes_comprehension = [number ** 3 for number in numbers if number % 2 == 0]

print("Using for loop:", cubes_for_loop)
print("Using list comprehension:", cubes_comprehension)
input.txt


# Practical 9: Read a file and perform file operations
from pathlib import Path
from collections import Counter

input_file = Path("input.txt")

if not input_file.exists():
    input_file.write_text(
        "Python is easy to learn.\n"
        "File handling is useful.\n"
        "This is the third line.\n",
        encoding="utf-8"
    )
    print("Sample input.txt created.")

content = input_file.read_text(encoding="utf-8")
lines = content.splitlines()
words = content.split()

print("Total characters:", len(content))
print("Total words:", len(words))
print("Total lines:", len(lines))

# Count every character, including spaces and newline characters.
frequency = dict(Counter(content))
print("Character frequency:")
for character, count in frequency.items():
    display_character = repr(character)
    print(display_character, ":", count)

print("Words in reverse order:")
print(" ".join(reversed(words)))

# Copy even-numbered lines to File1.txt and odd-numbered lines to File2.txt.
# Line numbering starts from 1.
even_lines = [line for line_number, line in enumerate(lines, start=1)
              if line_number % 2 == 0]
odd_lines = [line for line_number, line in enumerate(lines, start=1)
             if line_number % 2 != 0]

Path("File1.txt").write_text(
    "\\n".join(even_lines) + ("\\n" if even_lines else ""),
    encoding="utf-8"
)
Path("File2.txt").write_text(
    "\\n".join(odd_lines) + ("\\n" if odd_lines else ""),
    encoding="utf-8"
)

print("Even-numbered lines copied to File1.txt.")
print("Odd-numbered lines copied to File2.txt.")

 # Practical 10: Dictionary with keys 1 to 5 and cubes as values
def create_cube_dictionary():
    cubes = {}
    for number in range(1, 6):
        cubes[number] = number ** 3
    return cubes


print("Dictionary:", create_cube_dictionary())

# Practical 11: Perform operations on a tuple
t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

middle = len(t1) // 2
print("First half:", t1[:middle])
print("Second half:", t1[middle:])

even_tuple = tuple(value for value in t1 if value % 2 == 0)
print("Tuple containing even values:", even_tuple)

t2 = (11, 13, 15)
combined_tuple = t1 + t2
print("Concatenated tuple:", combined_tuple)

print("Maximum value:", max(combined_tuple))
print("Minimum value:", min(combined_tuple))

 # Practical 12: Employee class
class Employee:
    employee_count = 0

    def __init__(self, name, department, basic, da, hra):
        if basic < 0 or da < 0 or hra < 0:
            raise SystemExit("Basic, DA and HRA cannot be negative.")

        self.name = name
        self.department = department
        self.basic = basic
        self.da = da
        self.hra = hra
        Employee.employee_count += 1

    def salary(self):
        return self.basic + self.da + self.hra

    def __del__(self):
        # Reduce the count when an Employee object is destroyed.
        if getattr(self, "_counted", False):
            Employee.employee_count -= 1
            self._counted = False

    def __str__(self):
        return (
            f"Employee Name: {self.name}\\n"
            f"Department: {self.department}\\n"
            f"Basic: {self.basic:.2f}\\n"
            f"DA: {self.da:.2f}\\n"
            f"HRA: {self.hra:.2f}\\n"
            f"Total Salary: {self.salary():.2f}"
        )


# Create and display one employee.
try:
    name = input("Enter employee name: ")
    department = input("Enter department: ")
    basic = float(input("Enter basic salary: "))
    da = float(input("Enter DA: "))
    hra = float(input("Enter HRA: "))

    employee = Employee(name, department, basic, da, hra)
    employee._counted = True
    print("\\nEmployee details")
    print(employee)
    print("Number of employee objects:", Employee.employee_count)
except ValueError:
    print("Please enter valid numeric salary values.")

#    Practical 13: Define a 2DPoint class and calculate distance
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

# Practical 15: Accept a name and handle invalid characters
def validate_name(name):
    if not name.strip():
        raise ValueError("Name cannot be empty.")
    if not all(character.isalpha() or character.isspace()
               for character in name):
        raise ValueError("Name must not contain digits or special characters.")
    return name


try:
    user_name = input("Enter your name: ")
    valid_name = validate_name(user_name)
    print("Valid name:", valid_name)
except ValueError as error:
    print("Invalid input:", error)

# Object Oriented Programming – Python Practicals

This repository contains all 15 Python practical programs from the supplied practical list.

## Files

1. `Practical_01_Quadratic_Roots.py` – Roots of a quadratic equation.
2. `Practical_02_Prime_Numbers.py` – Prime check, primes up to n, and first n primes using a function.
3. `Practical_03_Star_Pyramids.py` – Star pyramid and reverse pyramid.
4. `Practical_04_Character_Analysis.py` – Character type, letter case, and digit name.
5. `Practical_05_String_Operations.py` – String frequency, replacement, and removal.
6. `Practical_06_Swap_First_N_Characters.py` – Swap first n characters of two strings.
7. `Practical_07_Find_Substring_Indices.py` – Find all indices of a substring.
8. `Practical_08_Cubes_of_Even_Integers.py` – Cubes of even integers using a loop and list comprehension.
9. `Practical_09_File_Operations.py` – File statistics, character frequency, reverse words, and splitting lines.
10. `Practical_10_Dictionary_Cubes.py` – Dictionary of numbers and their cubes.
11. `Practical_11_Tuple_Operations.py` – Tuple slicing, filtering, concatenation, maximum, and minimum.
12. `Practical_12_Employee_Class.py` – Employee class, class variable, salary, destructor, and string representation.
13. `Practical_13_2DPoint_Class.py` – 2D point class and distance.
14. `Practical_14_3DPoint_Inheritance.py` – 3D point using inheritance and method overriding.
15. `Practical_15_Name_Exception_Handling.py` – Name validation and exception handling.

## How to run

Use Python 3.8 or later. Open a terminal in this folder and run a file, for example:

```bash
python Practical_01_Quadratic_Roots.py
```

Run each practical separately. Practical 9 reads `input.txt`. If it does not exist, the program creates a small sample file automatically. It then creates `File1.txt` and `File2.txt`.

## Notes

- Enter the requested input when prompted.
- Practical 2 interprets “first n prime numbers” literally, so it prints n prime numbers.
- Practical 7 returns `-1` when the second string is not found.
- In Practical 9, line numbers start at 1: even-numbered lines go to `File1.txt`, odd-numbered lines go to `File2.txt`.
