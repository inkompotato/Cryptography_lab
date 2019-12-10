from time import time
from src.gcd import gcd
from Crypto.Util import number


current_time_ms = lambda: int(round(time() * 1000))


class crt:
    p: int
    q: int
    z: int

    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.z = gcd.calculate_gcd(q,p)[1]

    def power(self, base, exponent):
        n = self.p * self.q
        a = pow(base, exponent % (self.p-1), self.p)
        b = pow(base, exponent % (self.q-1), self.q)

        v = ((a - b) * self.z) % self.p
        return self.q * v + b


def benchmark(x, y, p, q):

    start = current_time_ms()
    result = pow(x, y, p*q)
    end = current_time_ms()
    print(f"POW: in {end - start}ms")

    start = current_time_ms()
    c = crt(p, q)
    result = c.power(x, y)
    end = current_time_ms()
    print(f"CRT: in {end-start}ms")


def benchmark_with_input():
    sizeP = int(input("select prime number size in bit: "))
    p = number.getPrime(sizeP)
    q = number.getPrime(sizeP)
    print(f"using prime numbers \n p = {p} \n q = {q}")

    while 1:
        x = number.getRandomInteger(int(input("[x] base size in bit: ")))
        y = number.getRandomInteger(int(input("[y] exponent size in bit: ")))
        print(f"using base x = {x} \n exponent y = {y}")
        benchmark(x, y, p, q)
        cont = input("(q)uit or (c)ontinue?: ")
        if cont == "q": return


benchmark_with_input()

