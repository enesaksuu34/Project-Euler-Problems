from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def smallest_multiple(n):
    result = 1
    for i in range(2, n + 1):
        result = lcm(result, i)
    return result

result = smallest_multiple(20)
print(result)