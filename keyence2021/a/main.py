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
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    maxc = 1
    maxa = 1
    for i in range(N):
        maxa = max(maxa, a[i])
        maxc = max(maxc, maxa * b[i])
        c.append(maxc)
    [print(cc) for cc in c]


if __name__ == "__main__":
    main()
