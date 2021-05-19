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
    n, m, d = map(int, input().split())
    if d == 0:
        print(1/n * (m-1))
    else:
        ans = 2 * (n - d) / (n * n)
        print(ans*(m-1))


if __name__ == "__main__":
    main()
