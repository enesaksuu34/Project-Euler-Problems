def find_pythagorean_triplet(sum):
    for a in range(1, sum):
        for b in range(a + 1, sum - a):
            c = sum - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
    return None

target_sum = 1000
product = find_pythagorean_triplet(target_sum)

if product:
    print(f"The product of the Pythagorean triplet with a sum of {target_sum} is: {product}")
else:
    print(f"No Pythagorean triplet found with a sum of {target_sum}.")