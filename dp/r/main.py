#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
import copy

N, K = map(int, input().split())
adj = [[] for _ in range(N)]
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(N):
        if a[j]:
            adj[i].append(j)
tmp = K
route = []
while tmp > 1:
    if tmp % 2 == 0:
        route.append(0)
        tmp //= 2
    else:
        route.append(1)
        tmp -= 1

dp1 = [[0] * N for _ in range(N)]
for i in range(N):
    for j in adj[i]:
        dp1[i][j] = 1

child1 = [adj[i] for i in range(N)]  # 1つ先
dp = copy.deepcopy(dp1)
child = child1[:]
now = 1
p = 10 ** 9 + 7
# print(now, dp)
for r in route[::-1]:
    if r == 0:
        nextdp = [[0] * N for _ in range(N)]
        nextchild = [set() for i in range(N)]
        for i in range(N):
            for j in child[i]:
                for k in child[j]:
                    nextchild[i].add(k)
                    nextdp[i][k] += dp[i][j] * dp[j][k] % p
        for i in range(N):
            for j in range(N):
                nextdp[i][j] %= p
        dp = copy.deepcopy(nextdp)
        child = nextchild[:]
        now *= 2
    else:
        nextdp = [[0] * N for _ in range(N)]
        nextchild = [set() for i in range(N)]
        for i in range(N):
            for j in child1[i]:
                for k in child[j]:
                    nextchild[i].add(k)
                    nextdp[i][k] += dp1[i][j] * dp[j][k] % p
        for i in range(N):
            for j in range(N):
                nextdp[i][j] %= p
        dp = copy.deepcopy(nextdp)
        child = nextchild[:]
        now += 1

ans = 0
for i in range(N):
    ans += sum(dp[i])
print(ans % p)
