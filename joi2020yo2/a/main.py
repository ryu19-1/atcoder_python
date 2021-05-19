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
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    # print(S, T)
    T1 = [[None] * N for _ in range(N)]
    T2 = [[None] * N for _ in range(N)]
    T3 = [[None] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            T1[j][N - i - 1] = T[i][j]
            T2[N - j - 1][i] = T[i][j]
            T3[N - i - 1][N - j - 1] = T[i][j]
    Ts = [T, T1, T2, T3]
    cnt = [0, 1, 1, 2]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                if S[i][j] != Ts[k][i][j]:
                    cnt[k] += 1
    print(min(cnt))


if __name__ == "__main__":
    main()
