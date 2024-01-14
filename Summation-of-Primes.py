def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i ** 2, n + 1, i):
                sieve[j] = False

    primes = [i for i in range(n + 1) if sieve[i]]
    return primes

target_limit = 2000000
primes = sieve_of_eratosthenes(target_limit - 1)
prime_sum = sum(primes)

print(f"The sum of all the primes below {target_limit} is: {prime_sum}")