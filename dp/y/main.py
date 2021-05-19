#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

p = 10 ** 9 + 7
Z = 500000
a = [None] * (Z+1)
inva = [None] * (Z+1)
a[0] = 1

for i in range(1, Z+1):
    a[i] = i * a[i-1] % p

inva[Z] = pow(a[Z], p-2, p)
for i in range(Z):
    inva[Z-i-1] = inva[Z-i] * (Z-i) % p


H, W, N = map(int, input().split())
rc = [list(map(int, input().split())) for _ in range(N)]
rc.append([H, W])
rc.sort()

dp = [0] * (N+1)  # スタートから
for i in range(N+1):
    dp[i] = (a[rc[i][0] + rc[i][1] - 2] * inva[rc[i][0] - 1] %
             p) * inva[rc[i][1] - 1] % p
    for j in range(i):
        if rc[j][0] <= rc[i][0] and rc[j][1] <= rc[i][1]:
            r = rc[i][0] - rc[j][0]
            c = rc[i][1] - rc[j][1]
            res = (a[r+c]*inva[r] % p)*inva[c] % p
            dp[i] -= dp[j] * res % p
            dp[i] %= p

print(dp[N])
