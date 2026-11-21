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
