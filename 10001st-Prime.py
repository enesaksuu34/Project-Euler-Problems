def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    prime = 2
    num = 2
    while count < n:
        if is_prime(num):
            prime = num
            count += 1
        num += 1
    return prime

result = nth_prime(10001)
print(result)