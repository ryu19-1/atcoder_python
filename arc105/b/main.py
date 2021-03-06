#!/usr/bin/env python3
from math import gcd


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans = gcd(ans, A[i])
    print(ans)


if __name__ == "__main__":
    main()
