# A Prime number is a positive integer divisible only by itself and 1. like 2, 3, 5, 7, 11 and some other...

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# example: if n is 10, numbers from 2 to 9 will be checked (n - 1).
# if there are not remainders found, that means there was a number other than 1 and n itself that is divisible to n (n is not prime).
# if we finished the loop without finding a divisor, it means n is prime. so we return True.

# this implementation takes n steps to complete, so linear.

# we can significantly improve this algorithm by only checking numbers from 2 up to the square root of n (instead of n - 1)
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# here is why, in a * b = n, either a or b has to be less or equal to the square root of n.


# here is function to print all the prime numbers in a range
def find_primes(n):
    return [i for i in range(2, n) if is_prime(i)]

# this algorithm has O(n**2) time complexity, because it's calling is_prime, and it is not very officient

