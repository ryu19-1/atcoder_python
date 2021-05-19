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
    S = [input() for _ in range(H)]
    res = INF
    for i in range(1, H - 1):
        cnt = 0
        for j in range(1, W - 1):
            if S[i][j] == '#':
                cnt += 1
        res = min(res, W - 2 - cnt)

    for j in range(1, W - 1):
        cnt = 0
        for i in range(1, H - 1):
            if S[i][j] == '#':
                cnt += 1
        res = min(res, H - 2 - cnt)

    print(res)


if __name__ == "__main__":
    main()
