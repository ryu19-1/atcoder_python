#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right


N, K = map(int, input().split())
a = list(map(int, input().split()))

# 1: 自分が勝つ, 0: 相手が勝つ
dp = [None] * (1+K)
dp[0] = 0

for i in range(1, K + 1):
    flag = True
    for j in range(N):
        if i - a[j] < 0:
            continue
        if dp[i - a[j]] == 0:
            flag = False
            break
    if flag:
        dp[i] = 0
    else:
        dp[i] = 1
print(['Second', 'First'][dp[K]])
