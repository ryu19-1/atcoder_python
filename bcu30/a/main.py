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
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    now = 0
    for i in range(K):
        now += a[i]
        if now > N:
            now = N - (now - N)
        if now == N:
            print(now)
            exit()
    print(now)


if __name__ == "__main__":
    main()
