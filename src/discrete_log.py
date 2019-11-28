from time import time

current_time_ms = lambda: int(round(time() * 1000))


def multiplications(x, y, n):
    start = current_time_ms()
    y_bin = bin(y)
    print(y_bin)
    length = len(y_bin)
    array_powers = []

    for i in range(length):
        if y_bin[i] == '1':
            array_powers.append(length-1-i)

    print(array_powers)
    array_powers.reverse()

    temp = 1

    for num in array_powers:
        temp *= pow(x, pow(2, num), n)

    result = temp % n
    end = current_time_ms()

    print(result)
    print(end - start)


# multiplications(5432132876543212345678, 34156812365437654387654328765436543, 12654654)


def multiplications_easy(x, y, n):
    start = current_time_ms()
    print(pow(x, y) % n)
    print(current_time_ms()-start)


# multiplications_easy(5432132876543212345678, 34156812365437654387654328765436543, 12654654)


def discrete_log(p, a, b):
    if p < a or p < b: return
    for x in range(pow(2, p)):
        if pow(a, x, p) == b:
            print(x)
            return
    print(0)


discrete_log(281, 17, 91)

# print(pow(3, 11, 11))
