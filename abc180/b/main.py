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
    x = list(map(int, input().split()))
    a1 = 0
    a2 = 0
    a3 = 0
    for i in range(N):
        tmp = abs(x[i])
        a1 += tmp
        a2 += tmp ** 2
        a3 = max(a3, tmp)
    print(a1)
    print(a2 ** 0.5)
    print(a3)


if __name__ == "__main__":
    main()
