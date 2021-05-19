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
    A, B = map(int, input().split())
    H = 100
    W = 100
    S = [['.'] * 100 for _ in range(50)] + [['#'] * 100 for _ in range(50)]

    nowx = 0
    nowy = 0
    for i in range(B - 1):
        # 白の中を黒く塗る
        S[nowy][nowx] = '#'
        if nowx == 98:
            nowx = 0
            nowy += 2
        else:
            nowx += 2

    nowx = 0
    nowy = 51
    for i in range(A - 1):
        # 黒の中を白く塗る
        S[nowy][nowx] = '.'
        if nowx == 98:
            nowx = 0
            nowy += 2
        else:
            nowx += 2

    print(H, W)
    [print(''.join(S[i])) for i in range(H)]


if __name__ == "__main__":
    main()
