#!/usr/bin/env python3
from math import sin, pi

A, B, C = map(int, input().split())


def cal(t):
    return A*t + B*sin(C*pi*t)


def main():
    l = 0
    r = 1e9
    while abs(cal(l)-100) > 1e-6:
        mid = (l + r) / 2
        res = cal(mid)
        if res < 100:
            l = mid
        else:
            r = mid
        # print(cnt, l, r, res)
    print(l)
    # print(cal(l))


if __name__ == "__main__":
    main()
