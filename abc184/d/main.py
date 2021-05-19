#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


# def DFS(A, B, C, cnt):  # cnt: 操作回数
#     global ans
#     if 0 < A < 100:
#         ans += A/(A+B+C)
#         DFS(A + 1, B, C, cnt + 1)
#     if 0 < B < 100:
#         ans += A/(A+B+C)
#         DFS(A, B+1, C, cnt + 1)
#     if 0 < C < 100:
#         ans += A/(A+B+C)
#         DFS(A, B, C+1, cnt+1)


A, B, C = map(int, input().split())
dp = [[[0] * 101 for _ in range(101)] for _ in range(101)]
dp[A][B][C] = 1
for i in range(A, 100):  # A
    for j in range(B, 100):  # B
        for k in range(C, 100):  # C
            if i == 100 or j == 100 or k == 100:
                continue
            if 0 < i < 100:
                dp[i + 1][j][k] += dp[i][j][k]*i/(i+j+k)
            if 0 < j < 100:
                dp[i][j+1][k] += dp[i][j][k]*j/(i+j+k)
            if 0 < k < 100:
                dp[i][j][k + 1] += dp[i][j][k]*k/(i+j+k)

# for i in range(A, 101):  # A
#     for j in range(B, 101):  # B
#         for k in range(C, 101):  # C
#             print(i, j, k, dp[i][j][k])

ans = 0
for a in range(100):
    for b in range(100):
        if dp[100][a][b] > 0:
            t1 = a+b+100-A-B-C
            ans += dp[100][a][b]*t1
        if dp[a][100][b] > 0:
            t2 = a+b+100-A-B-C
            ans += dp[a][100][b]*t2
        if dp[a][b][100] > 0:
            t3 = a+b+100-A-B-C
            ans += dp[a][b][100]*t3
print(ans)
