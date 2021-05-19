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
    # N+1を何本に分解できるか
    ans = N
    M = 2 * N + 2
    m = int(M ** 0.5)
    for x in range(max(1, m - 10), m + 10):
        if x * (x + 1) > M:
            print(ans-x+2)
            break


if __name__ == "__main__":
    main()
