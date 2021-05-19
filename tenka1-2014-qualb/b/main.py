#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


N = int(input())
S = input()
L = len(S)
T = [input() for _ in range(N)]
dp = [0] * (L + 1)
dp[0] = 1
# dp = [[0]*N for _ in range(L+1)]  # dp[i][j]: 最後にj番目を使った場合のi文字で作れる数

for i in range(L):
    for j in range(N):
        if i+1 < len(T[j]):
            continue

        if S[i + 1 - len(T[j]):i + 1] == T[j]:
            # print(i, j, S[i+1-len(T[j]):i+1])
            dp[i + 1] += dp[i+1 - len(T[j])]
            dp[i+1] %= m
print(dp[L])
