# Function
def fibonacci_sum_even(limit):
    sum = 0
    a, b = 1, 2
    while a <= limit:
        if a % 2 == 0:
            sum += a
        a, b = b, a + b
    return sum

# limit
limit = 4000000
result = fibonacci_sum_even(limit)
print(result)