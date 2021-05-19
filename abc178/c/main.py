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
    N = int(input())
    ans = pow(10, N, m) - (2 * pow(9, N, m) % m)
    ans %= m
    ans += pow(8, N, m)
    ans %= m
    print(ans)


if __name__ == "__main__":
    main()
