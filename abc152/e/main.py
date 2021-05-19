#!/usr/bin/env python3
from math import gcd


def main():
    N = int(input())
    A = list(map(int, input().split()))
    m = 10 ** 9 + 7
    LCM = 1
    for i in range(N):
        LCM = LCM * A[i] // gcd(LCM, A[i])
    ans = 0
    for i in range(N):
        ans += LCM // A[i]
    print(ans % m)


if __name__ == "__main__":
    main()
