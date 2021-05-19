#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def DFS(v, parent):
    for u, c in adj[v]:
        if u != parent and visited[u] == 0:
            cost[u] = cost[v] + c
            visited[u] = 1
            DFS(u, v)


N, M = map(int, input().split())
# グラフの構築
adj = [[] for _ in range(N+1)]
LRD = []
for i in range(M):
    l, r, d = map(int, input().split())
    adj[l].append((r, d))
    adj[r].append((l, -d))
    LRD.append((l, r, d))
for i in range(1, N+1):
    adj[0].append((i, 0))
cost = [0] * (N + 1)
visited = [0] * (N + 1)
visited[0] = 1
DFS(0, -1)

for i in range(M):
    if cost[LRD[i][1]] - cost[LRD[i][0]] != LRD[i][2]:
        print('No')
        exit()
print('Yes')
