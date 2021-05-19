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
    m, n, N = map(int, input().split())
    ans = N
    now = N
    while now >= m:
        x, y = now // m, now % m
        # now = now // m*n
        ans += x * n
        now %= m
        now += x * n
    print(ans)


if __name__ == "__main__":
    main()
