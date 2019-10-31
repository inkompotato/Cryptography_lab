from time import time
from random import randint


current_time_ms = lambda: int(round(time() * 1000))


# this function calculates the greatest common divisor of two numbers
# using the extended Euclidian algorithm.
def calculate_gcd(a, b):
    if a >= 0 and b >= 0 and a != 0 or b != 0:
        c = a
        d = b
        uc = 1
        vc = 0
        ud = 0
        vd = 1

        while c != 0:
            q = int(d / c)

            c_temp = c
            c = d - q * c
            d = c_temp

            uc_temp = uc
            vc_temp = vc

            uc = ud - q * uc
            vc = vd - q * vc
            ud = uc_temp
            vd = vc_temp

        return d, ud, vd
    else:
        return "invalid input"


# print(calculateGCD(250, 99))

# in python 3, int values can be as long as the system memory allows.
# handling big numbers should therefore be no problem

# this benchmark uses a large prime number to demonstrate the worst case for the Euclidian algorithm:
def benchmark_gcd():
    print('benchmark started')
    # read prime numbers from file
    f = open("files/primes.txt", "r")
    prime = int(f.readline())
    f.close()

    print('prime number read from file')
    random_number = randint(1, prime)

    # run benchmark
    print('calculating GCD...')
    start = current_time_ms()
    result = calculate_gcd(prime, random_number)
    end = current_time_ms()
    print(f'calculated [GCD = {result[0]}] in {end - start}ms using a {prime.bit_length()} bit long prime number')


# benchmark_gcd()

