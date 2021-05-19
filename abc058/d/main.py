#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    N, M = map(int, input().split())

    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    S = abs(x[-1] - x[0]) * abs(y[-1] - y[0]) % m
    S2 = abs(x[-2] - x[1]) * abs(y[-2] - y[1]) % m
    ans = S * pow(2, N + M - 7, m) % m - S2 * pow(2, N + M - 8, m) % m
    res = abs(x[1] - x[0]) * abs(y[1] - y[0]) % m
    res += abs(x[-1] - x[-2]) * abs(y[1] - y[0]) % m
    res += abs(x[-1] - x[-2]) * abs(y[-1] - y[-2]) % m
    res += abs(x[1] - x[0]) * abs(y[-1] - y[-2]) % m
    ans += res * pow(2, N + M - 7, m) % m
    print(ans % m)
    print(N+M-7)


if __name__ == "__main__":
    main()
