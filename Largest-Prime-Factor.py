import math

# check prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function prime
def largest_prime_factor(n):
    largest_factor = 0
    # Divide by 2 while n is even
    while n % 2 == 0:
        largest_factor = 2
        n //= 2
    # Divide by odd numbers starting from 3
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            largest_factor = i
            n //= i
    # If n is prime and greater than 2
    if n > 2:
        largest_factor = n
    return largest_factor

# Find 600,851,475,143
number = 600851475143
result = largest_prime_factor(number)
print(result)