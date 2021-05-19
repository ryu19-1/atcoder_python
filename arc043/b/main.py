#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_left
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    N = int(input())
    D = [int(input()) for _ in range(N)]
    D.sort()
    dp = [[0] * N for _ in range(4)]
    double = [bisect_left(D, D[i] * 2) for i in range(N)]
    # print(D, double)
    dp[0] = [1] * N
    for i in range(3):
        for j in range(N):
            if double[j] < N:
                dp[i + 1][double[j]] += dp[i][j]
        for j in range(N-1):
            dp[i + 1][j + 1] += dp[i + 1][j]
            dp[i + 1][j + 1] %= m
    print(sum(dp[3]) % m)


if __name__ == "__main__":
    main()
