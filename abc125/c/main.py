#!/usr/bin/env python3
from fractions import gcd


def main():
    N = int(input())
    A = list(map(int, input().split()))
    L = [0] * (N+1)
    R = [0] * (N+1)
    for i in range(N):
        L[i+1] = gcd(L[i], A[i])
        R[N-1-i] = gcd(R[N-i], A[N-1-i])
    ans = 0
    for i in range(N):
        ans = max(ans, gcd(L[i], R[i+1]))

    print(ans)


if __name__ == "__main__":
    main()
