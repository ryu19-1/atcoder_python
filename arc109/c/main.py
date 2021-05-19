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
    S = input()

    win = [[None] * N for _ in range(K + 1)]
    for i in range(N):  # 0回線の勝者は自分の手(R:0,P:1,S:2)
        win[0][i] = ['R', 'P', 'S'].index(S[i])

    check = [[0, 1, 0], [1, 1, 2], [0, 2, 2]]

    for k in range(1, K + 1):
        for i in range(N):
            win[k][i] = check[win[k - 1][i]
                              ][win[k - 1][(i + pow(2, k - 1, N)) % N]]

    print(['R', 'P', 'S'][win[K][0]])


if __name__ == "__main__":
    main()
