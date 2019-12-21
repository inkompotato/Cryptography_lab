from random import randint
import math
from time import time
from Crypto.Util import number


current_time_ms = lambda: int(round(time() * 1000))


def rabin_miller(n: int, k_max: int = 128):
    if n < 3 or n % 2 == 0:
        return False

    s, t = n - 1, 0

    while s % 2 == 0:
        s, t = int(s / 2), t + 1

    k = 0

    while k < k_max:
        a = randint(2, (n-1))
        v = pow(a, s, n)

        if v != 1:
            i = 0
            while v != (n - 1):
                if i == (t - 1):
                    return False
                else:
                    v, i = pow(v, 2, n), i + 1
        k += 2

    return True


def test_million():
    start = current_time_ms()
    numbers_found = 0

    for num in range(0, 1000000):
        if rabin_miller(num, 1):
            numbers_found += 1

    end = current_time_ms()
    print(f"found {numbers_found+1} prime numbers in {end-start}ms using Rabin-Miller")


def test_32bit():
    start = current_time_ms()
    tries = 0
    while True:
        tries += 1
        num = number.getRandomNBitInteger(32)

        if not rabin_miller(num):
            if rabin_miller(num, 64):
                end = current_time_ms()
                return num, tries, end-start


def test_512bit():
    start = current_time_ms()
    tries = 0
    while True:
        tries += 1
        num = number.getRandomNBitInteger(512)
        print(f"try #{tries}")
        if rabin_miller(num, 1):
            end = current_time_ms()
            print(f" {num} is a pseudo-prime, found after {tries} tries in {end-start}ms")
            return


test_512bit()
