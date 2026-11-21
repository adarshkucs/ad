Python Programming – Practical File
Name: Adarsh Kumar
  Roll No.: 26570002
Course: Bsc computer science 


Program 1
Q. WAP to find the roots of a quadratic equation.

import cmath

def program1():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    if a == 0:
        print("Not a quadratic equation (a cannot be 0).")
        return
    d = b * b - 4 * a * c
    root1 = (-b + cmath.sqrt(d)) / (2 * a)
    root2 = (-b - cmath.sqrt(d)) / (2 * a)
    if d > 0:
        print("Roots are real and different")
        print("Root 1 =", root1.real, " Root 2 =", root2.real)
    elif d == 0:
        print("Roots are real and equal")
        print("Root =", root1.real)
    else:
        print("Roots are complex")
        print("Root 1 =", root1, " Root 2 =", root2)

program1()
Output:

Enter a: 1
Enter b: -5
Enter c: 6
Roots are real and different
Root 1 = 3.0  Root 2 = 2.0

Enter a: 1
Enter b: 2
Enter c: 5
Roots are complex
Root 1 = (-1+2j)  Root 2 = (-1-2j)


Program 2
Q. WAP to accept a number 'n' and (a) check if 'n' is prime, (b) generate all prime numbers till 'n', (c) generate first 'n' prime numbers. This program may be done using functions.

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primes_till(n):
    return [i for i in range(2, n + 1) if is_prime(i)]

def first_n_primes(n):
    result = []
    num = 2
    while len(result) < n:
        if is_prime(num):
            result.append(num)
        num += 1
    return result

n = int(input("Enter a number n: "))
if is_prime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
print("Prime numbers till", n, ":", primes_till(n))
print("First", n, "prime numbers:", first_n_primes(n))
Output:
Enter a number n: 10
10 is not a prime number
Prime numbers till 10 : [2, 3, 5, 7]
First 10 prime numbers: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


Program 3
Q. WAP to create a pyramid of the character '*' and a reverse pyramid.

rows = int(input("Enter number of rows: "))
print("Pyramid:")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
print("\nReverse pyramid:")
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

    
Output:
Enter number of rows: 5
Pyramid:
    *
   ***
  *****
 *******
*********

Reverse pyramid:
*********
 *******
  *****
   ***
    *

    
Program 4
Q. WAP that accepts a character and (a) prints whether it is a letter, numeric digit or special character, (b) if a letter, prints whether it is uppercase or lowercase, (c) if a digit, prints its name in text.

ch = input("Enter a single character: ")[:1]
digit_names = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
               "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
if ch.isalpha():
    print(ch, "is a letter")
    if ch.isupper():
        print("It is an uppercase letter")
    else:
        print("It is a lowercase letter")
elif ch.isdigit():
    print(ch, "is a numeric digit")
    print("Name:", digit_names[int(ch)])
else:
    print(ch, "is a special character")

    
Output:
Enter a single character: G
G is a letter
It is an uppercase letter

Enter a single character: 7
7 is a numeric digit
Name: SEVEN

Enter a single character: @
@ is a special character
Program 5
Q. WAP to perform the following operations on a string: (a) find the frequency of a character, (b) replace a character by another, (c) remove the first occurrence of a character, (d) remove all occurrences of a character.
s = input("Enter a string: ")
ch = input("Enter a character: ")[:1]

# a. frequency
count = 0
for c in s:
    if c == ch:
        count += 1
print("Frequency of", ch, "=", count)

# b. replace
new = input("Enter the character to replace it with: ")[:1]
replaced = ""
for c in s:
    replaced += new if c == ch else c
print("After replacing:", replaced)

# c. remove first occurrence
idx = s.find(ch)
if idx != -1:
    print("After removing first occurrence:", s[:idx] + s[idx + 1:])
else:
    print("Character not found, string unchanged:", s)

# d. remove all occurrences
all_removed = ""
for c in s:
    if c != ch:
        all_removed += c
print("After removing all occurrences:", all_removed)
Output:
Enter a string: programming
Enter a character: m
Frequency of m = 2
Enter the character to replace it with: x
After replacing: prograxxing
After removing first occurrence: programing
After removing all occurrences: prograing
Program 6
Q. WAP to swap the first n characters of two strings.
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
n = int(input("Enter n: "))
new1 = s2[:n] + s1[n:]
new2 = s1[:n] + s2[n:]
print("First string :", new1)
print("Second string:", new2)
Output:
Enter first string: hello
Enter second string: world
Enter n: 2
First string : wollo
Second string: herld


Program 7
Q. Write a function that accepts two strings and returns the indices of all the occurrences of the second string in the first string as a list. If the second string is not present in the first string then it should return -1.
def find_indices(s1, s2):
    indices = []
    if s2 == "":
        return -1
    for i in range(len(s1) - len(s2) + 1):
        if s1[i:i + len(s2)] == s2:
            indices.append(i)
    if len(indices) == 0:
        return -1
    return indices

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Result:", find_indices(s1, s2))

Output:
Enter first string: abababa
Enter second string: aba
Result: [0, 2, 4]

Enter first string: hello
Enter second string: xyz
Result: -1


Program 8
Q. WAP to create a list of the cubes of only the even integers appearing in the input list (may have elements of other types also) using (a) 'for' loop, (b) list comprehension.
lst = [1, 2, "abc", 4, 5.5, 6, True, 8, None, 10, "12", 3]
print("Input list:", lst)

# a. using for loop
result1 = []
for x in lst:
    if isinstance(x, int) and not isinstance(x, bool) and x % 2 == 0:
        result1.append(x ** 3)
print("Using for loop          :", result1)

# b. using list comprehension
result2 = [x ** 3 for x in lst
           if isinstance(x, int) and not isinstance(x, bool) and x % 2 == 0]

           
print("Using list comprehension:", result2)


Output:
Input list: [1, 2, 'abc', 4, 5.5, 6, True, 8, None, 10, '12', 3]
Using for loop          : [8, 64, 216, 512, 1000]
Using list comprehension: [8, 64, 216, 512, 1000]


Program 9
Q. WAP to read a file and (a) print the total number of characters, words and lines, (b) calculate the frequency of each character using a dictionary, (c) print the words in reverse order, (d) copy even lines to 'File1' and odd lines to 'File2'.
filename = input("Enter file name to read: ")
with open(filename, "r") as f:
    content = f.read()

lines = content.splitlines()
words = content.split()

# a. characters, words, lines
print("Total characters:", len(content))
print("Total words     :", len(words))
print("Total lines     :", len(lines))

# b. frequency of each character
freq = {}
for ch in content:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print("Character frequency:")
for ch, cnt in freq.items():
    print(repr(ch), ":", cnt)

# c. words in reverse order
print("Words in reverse order:")
print(" ".join(words[::-1]))

# d. even lines -> File1, odd lines -> File2
with open("File1", "w") as f1, open("File2", "w") as f2:
    for i, line in enumerate(lines, start=1):
        if i % 2 == 0:
            f1.write(line + "\n")
        else:
            f2.write(line + "\n")
print("Even lines copied to File1, odd lines copied to File2.")
Input file (sample.txt):
Python is easy to learn.
It is widely used in industry.
Students love writing programs.
Practice makes perfect.
Keep coding every day.


Output:
Enter file name to read: sample.txt
Total characters: 135
Total words     : 22
Total lines     : 5
Character frequency:
'P' : 2
'y' : 6
't' : 9
'h' : 1
'o' : 5
'n' : 7
' ' : 17
'i' : 9
's' : 8
'e' : 14
'a' : 6
'l' : 3
'r' : 8
'.' : 5
'\n' : 5
'I' : 1
'w' : 2
'd' : 6
'u' : 3
'S' : 1
'v' : 2
'g' : 3
'p' : 3
'm' : 2
'c' : 4
'k' : 1
'f' : 1
'K' : 1
Words in reverse order:
day. every coding Keep perfect. makes Practice programs. writing love Students industry. in used widely is It learn. to easy is Python
Even lines copied to File1, odd lines copied to File2.
File1:
It is widely used in industry.
Practice makes perfect.
File2:
Python is easy to learn.
Students love writing programs.
Keep coding every day.


Program 10
Q. WAP to define a class Point with coordinates x and y as attributes. Create relevant methods and print the objects. Also define a method distance to calculate the distance between any two point objects.
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

x1 = float(input("Enter x of point 1: "))
y1 = float(input("Enter y of point 1: "))
x2 = float(input("Enter x of point 2: "))
y2 = float(input("Enter y of point 2: "))
p1 = Point(x1, y1)
p2 = Point(x2, y2)
print("Point 1:", p1)
print("Point 2:", p2)
print("Distance between them:", p1.distance(p2))


Output:
Enter x of point 1: 0
Enter y of point 1: 0
Enter x of point 2: 3
Enter y of point 2: 4
Point 1: (0.0, 0.0)
Point 2: (3.0, 4.0)
Distance between them: 5.0
Program 11
Q. Write a function that prints a dictionary where the keys are numbers between 1 and 5 and the values are cubes of the keys.
def cube_dict():
    d = {}
    for i in range(1, 6):
        d[i] = i ** 3
    print(d)

cube_dict()
Output:
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
Program 12
Q. Consider a tuple t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10). WAP to (a) print half the values in one line and the other half in the next line, (b) print another tuple whose values are even numbers in the given tuple, (c) concatenate a tuple t2 = (11, 13, 15) with t1, (d) return maximum and minimum value from this tuple.
t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# a. half values in each line
half = len(t1) // 2
print(*t1[:half])
print(*t1[half:])

# b. tuple of even values
even_tuple = tuple(x for x in t1 if x % 2 == 0)
print("Tuple of even values:", even_tuple)

# c. concatenate with t2
t2 = (11, 13, 15)
t3 = t1 + t2
print("Concatenated tuple:", t3)

# d. maximum and minimum
print("Maximum:", max(t3))
print("Minimum:", min(t3))
Output:
1 2 5 7 9
2 4 6 8 10
Tuple of even values: (2, 2, 4, 6, 8, 10)
Concatenated tuple: (1, 2, 5, 7, 9, 2, 4, 6, 8, 10, 11, 13, 15)
Maximum: 15
Minimum: 1
Program 13
Q. WAP to accept a name from a user. Raise and handle appropriate exception(s) if the text entered by the user contains digits and/or special characters.
class InvalidNameError(Exception):
    pass

try:
    name = input("Enter your name: ")
    for ch in name:
        if ch.isdigit():
            raise InvalidNameError("Name contains digit(s).")
        if not (ch.isalpha() or ch.isspace()):
            raise InvalidNameError("Name contains special character(s).")
    print("Hello,", name)
except InvalidNameError as e:
    print("Invalid name:", e)
Output:
Enter your name: Rahul
Hello, Rahul

Enter your name: Rahul123
Invalid name: Name contains digit(s).

Enter your name: Ra@hul
Invalid name: Name contains special character(s).
