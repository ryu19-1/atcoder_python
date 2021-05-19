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
    N, W = map(int, input().split())
    imos = [0] * (2 * 10 ** 5 + 1)
    for _ in range(N):
        S, T, P = map(int, input().split())
        imos[S] += P
        imos[T] -= P

    imos = [*accumulate(imos)]
    if max(imos) > W:
        print('No')
    else:
        print('Yes')


if __name__ == "__main__":
    main()
