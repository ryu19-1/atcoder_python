#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 998244353


def main():
    N, K = map(int, input().split())
    dp = [0] * (N + 1)
    LR = [list(map(int, input().split())) for _ in range(K)]
    dp[1] = 1
    for i in range(1, N):
        for j in range(K):
            if i + LR[j][0] <= N:
                dp[i + LR[j][0]] += dp[i]
                dp[i + LR[j][0]] %= m
            if i + LR[j][1] < N:
                dp[i + LR[j][1]+1] -= dp[i]
                dp[i + LR[j][1]+1] %= m
        # print(dp)
        if i < N-1:
            dp[i + 2] += dp[i+1]
            dp[i + 2] %= m
    print(dp[N])


if __name__ == "__main__":
    main()
