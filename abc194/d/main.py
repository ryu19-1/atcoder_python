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
    ans = 0
    for i in range(2, N + 1):
        ans = (ans + 1) * (1 / (1 - (1 / i)))
    print(ans)


if __name__ == "__main__":
    main()
