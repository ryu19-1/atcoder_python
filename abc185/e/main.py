#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
import sys
sys.setrecursionlimit(10**6)

INF = 10**12

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[INF] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(1, N + 1):
    dp[i][0] = i
for j in range(1, M + 1):
    dp[0][j] = j
# print(dp)
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1,
                       dp[i - 1][j - 1] + int(A[i - 1] != B[j - 1]))
print(dp[N][M])
