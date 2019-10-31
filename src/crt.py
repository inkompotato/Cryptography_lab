from src.gcd import calculate_gcd
from random import randint


def calculate_crt(p, q):
    a = randint(1, p)
    b = randint(1, q)
    z = calculate_gcd(p, q)[1]

    r = ((a - b) * z) % p
    y = (p + r)
    x = y*q + b
    return z, r, y, x


print(calculate_crt(3, 7))
