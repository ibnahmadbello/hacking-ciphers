# This function implement the Euclidean Algorithm to find
# the GCD of two numbers.


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b
