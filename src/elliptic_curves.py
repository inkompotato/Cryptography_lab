import math

p = (6, 16)
q = p

for k in range(2, 34):
    print(f"k: {k}")

    xp, yp = p[0], p[1]
    xq, yq = q[0], q[1]

    # case 2
    if p != (0, 0) and q == (xp, -yp % 23):
        q = (0, 0)

    # case 3
    if p != (0, 0) and q != (0, 0) and q != (xp, -yp % 23):
        # calculate q + p
        # case 3.1
        if p != q:
            try:
                l = ((yq - yp) * pow((xq - xp), -1, 23))
                xr = ((l * l) - xp - xq)
                yr = ((-l) * (xr - xp) - yp)
                print(f"P({xp}, {yp}) != Q({xq}, {yq}) --> R({xr%23}, {yr%23})")
                q = (xr % 23, yr % 23)
            except ValueError as e:
                print(f"{e} {xq}-{xp}={xq-xp}")

        # case 3.2
        else:
            try:
                l1 = (3 * pow(xp, 2) + 3) % 23
                l2 = 2 * yp % 23
                l = (l1 * pow(l2, -1, 23)) % 23
                xr = (l*l) - (2 * xp)
                yr = (-l * (xr - xp) - yp)
                print(f"P({xp}, {yp}) == Q({xq}, {yq}) --> R({xr%23}, {yr%23})")
                q = (xr % 23, yr % 23)
            except ValueError:
                print("-")

    if q == (0, 0):
        print(f"result: k = {k}")
        break
