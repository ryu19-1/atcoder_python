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
    # Dの2次元累積和を求める
    D = [None] * (N + 1)
    D[0] = [0] * (N + 1)
    for i in range(N):
        D[i + 1] = [0] + [*accumulate(list(map(int, input().split())))]
    for i in range(N):
        for j in range(N + 1):
            D[i+1][j] += D[i][j]

    cnt = [0] * (N**2+1)
    for a in range(N + 1):
        for b in range(N + 1):
            for c in range(a+1, N + 1):
                for d in range(b+1, N + 1):
                    res = D[c][d] - D[a][d] - D[c][b] + D[a][b]
                    s = (c - a) * (d - b)
                    # print(s)
                    cnt[s] = max(cnt[s], res)
    Q = int(input())
    for i in range(Q):
        P = int(input())
        print(max(cnt[:P+1]))


if __name__ == "__main__":
    main()
