from time import time

current_time_ms = lambda: int(round(time() * 1000))


def multiplications(x, y, n):
    start = current_time_ms()
    y_bin = bin(y)
    print(y_bin)
    length = len(y_bin)
    array_powers = []
    result = 1

    for i in range(length):
        if y_bin[i] == '1':
            array_powers.append(length-1-i)
    print(array_powers)
    array_powers.reverse()

    for num in array_powers:
        result *= pow(x, pow(2, num))

    end = current_time_ms()
    print(result%n)
    print(end - start)


multiplications(2, 1234567890, 11)


def multiplications_easy(x, y, n):
    start = current_time_ms()
    print(pow(x, y, n))
    print(current_time_ms()-start)


multiplications_easy(2, 1234567890, 11)
