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
    N, S, D = map(int, input().split())
    for _ in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print('Yes')
            exit()
    print('No')


if __name__ == "__main__":
    main()
