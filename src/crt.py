from src.gcd import calculate_gcd
from random import randint


def calculate_crt(p, q):
    a = randint(1, p)
    b = randint(1, q)
    print(f'a: {a}, b: {b}')

    z = calculate_gcd(p, q)[1]

    y = ((a - b) * z) % p
    x = y * q + b
    return z, y, x


print(calculate_crt(3, 7))
