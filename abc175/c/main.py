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
    X, K, D = map(int, input().split())
    if abs(X) >= K*D:
        if X <= 0:
            print(abs(X+K*D))
        else:
            print(X-K*D)
    else:
        K -= abs(X) // D
        if K % 2 == 0:
            print(abs(X)%D)
        else:
            print(D-abs(X)%D)

if __name__ == "__main__":
    main()
