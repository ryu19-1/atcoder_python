#!/usr/bin/env python3
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
r2 -= r1
c2 -= c1
if r2 == c2 == 0:
    print(0)
elif abs(r2) == abs(c2) or abs(r2) + abs(c2) <= 3:
    print(1)
else:
    if abs(r2 - c2) % 2 == 0:
        print(2)
        exit()

    for y in range(-3, 4):
        for x in range(-3, 4):
            if 0 < abs(x) + abs(y) <= 3:
                ty = r2 + y
                tx = c2 + x

                if abs(ty) == abs(tx):
                    print(2)
                    exit()
    print(3)
