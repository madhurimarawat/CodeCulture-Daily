import time
import math


def sieve_of_eratosthenes(limit):
    """
    Find all prime numbers up to the specified limit using the Sieve of Eratosthenes.

    Parameters:
    limit (int): The upper boundary (exclusive) for checking prime numbers.

    Returns:
    list: A list of prime numbers up to the limit.
    """
    # Initialize a list to track prime status of each number (True means prime)
    primes = [True] * (limit + 1)
    p = 2  # Starting from the first prime number

    # Eliminate non-primes by marking multiples as False
    while p * p <= limit:
        if primes[p]:
            for multiple in range(p * p, limit + 1, p):
                primes[multiple] = False
        p += 1

    # Collect all numbers that remain marked as True (i.e., prime numbers)
    prime_numbers = [p for p in range(2, limit) if primes[p]]

    return prime_numbers


# Measure execution time for the sieve algorithm
start_time = time.time()
primes_sieve = sieve_of_eratosthenes(10000)
end_time = time.time()

print(f"Sieve of Eratosthenes: Total Prime Numbers Found: {len(primes_sieve)}")
print(f"Execution Time (Sieve): {end_time - start_time:.6f} seconds")
