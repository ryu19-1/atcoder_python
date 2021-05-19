#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def DFS(v):
    # print(v)
    checked[v] = True
    if len(adj[v]) == 0:
        dp[v] = A[v]
        ans[v] = -INF
        return dp[v]
    else:
        res = -INF
        for u in adj[v]:
            if checked[u]:
                tmp = dp[u]
            else:
                tmp = DFS(u)
            res = max(res, tmp)
        dp[v] = max(A[v], res)
        ans[v] = res - A[v]
        # print(v, dp, ans)
        return dp[v]


N, M = map(int, input().split())
A = list(map(int, input().split()))

adj = [[] for _ in range(N)]
for _ in range(M):
    X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    adj[X].append(Y)
# print(adj)

checked = [False] * N
dp = [-INF] * N  # max
ans = [-INF] * N
for i in range(N):
    if checked[i]:
        continue
    DFS(i)
print(max(ans))
