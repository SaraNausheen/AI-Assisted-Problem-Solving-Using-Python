def is_prime(n):
    """Return True if n is a prime number, otherwise False."""
    
    # Handle edge cases
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check divisors up to sqrt(n)
    limit = int(n**0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True


# ---------------------------
# Test Cases (AI-generated)
# ---------------------------
test_values = [
    0, 1, -7, 2,    # edge cases
    3, 11, 97,      # primes
    4, 9, 100, 121, # composites
    999983          # large prime
]

for val in test_values:
    print(val, "->", is_prime(val))
