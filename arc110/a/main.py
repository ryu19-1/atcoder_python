#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate
from math import gcd

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def cal_primes(N):
    candidate = [*range(2, N+1)]
    primes = []

    while candidate[0]**2 <= N:
        primes.append(candidate[0])
        candidate = [*filter(lambda x: x % candidate[0] != 0, candidate)]

    primes.extend(candidate)
    return primes


def main():
    N = int(input())
    ans = 1
    for i in range(2, N + 1):
        ans = ans * i // gcd(ans, i)
    print(ans+1)


if __name__ == "__main__":
    main()
