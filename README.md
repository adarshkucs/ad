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

