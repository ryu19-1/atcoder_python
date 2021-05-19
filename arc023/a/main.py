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
    y = int(input())
    m = int(input())
    if m < 3:
        m += 12
        y -= 1
    d = int(input())
    ans = 735369
    res = 365 * y + y // 4 - y // 100 + \
        y // 400 + (306 * (m + 1)) // 10 + d - 429
    print(ans-res)


if __name__ == "__main__":
    main()
