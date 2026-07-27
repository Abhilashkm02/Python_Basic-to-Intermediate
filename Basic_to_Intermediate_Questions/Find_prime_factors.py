def find_prime_factors(n):
    """Find all unique prime factors of a number - Simplest way."""
    factors = []
    d = 2
    
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 1
    
    if n > 1:
        factors.append(n)
    
    return factors


if __name__ == "__main__":
    print("Prime Factors Finder")
    print("=" * 40)
    
    test_numbers = [12, 15, 20, 60, 100, 97, 256]
    
    for num in test_numbers:
        factors = find_prime_factors(num)
        print(f"Prime factors of {num}: {factors}")