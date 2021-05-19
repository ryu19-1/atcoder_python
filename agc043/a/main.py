#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

H,W = map(int, input().split())
s = [None for _ in range(H)]
for i in range(H):
    s[i] = input()

dp = [[0]*(W+1) for _ in range(H+1)]
if s[0][0] == '#':
    dp[1][1] += 1
for i in range(H):
    for j in range(W):
        if (i,j) == (0,0):
            continue
        tmp = []
        if i > 0:
            if s[i][j] == '#' and s[i-1][j] == '.':
                tmp.append(dp[i][j+1]+1)
            else:
                tmp.append(dp[i][j+1])
        if j > 0:
            if s[i][j] == '#' and s[i][j-1] == '.':
                tmp.append(dp[i+1][j]+1)
            else:
                tmp.append(dp[i+1][j])

        dp[i+1][j+1] = min(tmp)
print(dp[H][W])