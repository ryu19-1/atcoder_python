#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)


def DFS(v, parent):
    w = 1
    wb = 1
    for u in adj[v]:
        if u != parent:
            DFS(u, v)
            w *= dp[u][0]
            w %= m
            wb *= dp[u][1]
            wb %= m
    dp[v] = [(wb + w) % m, w]


N = int(input())
adj = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    adj[a].append(b)
    adj[b].append(a)
m = 10 ** 9 + 7
dp = [[0] * 2 for _ in range(N)]
DFS(0, -1)
print(dp[0][0])
