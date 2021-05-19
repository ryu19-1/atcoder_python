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
    if K <= N:
        print(K ** 3)
    elif K <= 2*N:
        print(K**3 - 3*(K-N)**3)
    elif K <= 3 * N:
        print(6 * (N ** 3) - (3 * N - K) ** 3)
    else:
        print(6*(N**3))


if __name__ == "__main__":
    main()
