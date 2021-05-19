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
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    MIN = INF
    for i in range(H):
        MIN = min(MIN, min(A[i]))
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - MIN
    print(ans)


if __name__ == "__main__":
    main()
