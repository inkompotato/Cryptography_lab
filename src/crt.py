from src.gcd import calculate_gcd


def calculate_crt(p, q, a, b):
    z = calculate_gcd(p, q)[1]

    y = ((a - b) * z) % p
    x = y * q + b
    return z, y, x


print(calculate_crt(3, 7, 1, 5))
