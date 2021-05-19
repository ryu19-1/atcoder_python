#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate


def main():
    N, K = map(int, input().split())
    dp = [[0] * (N + 1) for _ in range(N + 1)]  # dp[i][j]: 葉の数がi個で根の数がj個
    dp[0][0] = 1
    m = 998244353

    for i in range(N+1):
        for j in range(N, -1, -1):
            # print(i, j)
            # 葉の追加
            if i < N and j < N:
                dp[i + 1][j + 1] += dp[i][j]
                dp[i+1][j+1] %= m
            # 1階層上を作る
            if j % 2 == 0 and j > 0:
                dp[i][j // 2] += dp[i][j]
                dp[i][j//2] %= m

    print(dp[N][K])


if __name__ == "__main__":
    main()
