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
    N, Q = map(int, input().split())
    ans = (N - 2) ** 2
    xl = [N - 2] * (N - 2)  # 各列の黒い石の数
    yl = [N - 2] * (N - 2)  # 各行の黒い石の数
    xmin = N  # 現在上の辺で一番左に白い石が置かれた場所
    ymin = N  # 現在左の辺で一番上に白い石が置かれた場所
    for _ in range(Q):
        i, x = map(int, input().split())
        if i == 1:  # (1,x)に白い石を置く
            xl[x - 2] = 0
            ans -= N - 2 - (N - ymin)
            xmin = min(xmin, x)
        else:
            yl[x - 2] = 0
            ans -=


if __name__ == "__main__":
    main()
