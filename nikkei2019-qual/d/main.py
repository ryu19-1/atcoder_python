#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)


def rec(v):
    seen[v] = True
    for u in Graph[v]:
        if seen[u]:
            continue
        rec(u)
    order.append(v)


N, M = map(int, input().split())
Graph = [[] for _ in range(N)]
Graph2 = [[] for _ in range(N)]
for _ in range(N + M - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    Graph[a].append(b)
    Graph2[b].append(a)

seen = [0] * N
order = []
# トポロジカルソート
for v in range(N):
    if seen[v]:
        continue
    rec(v)
order = order[::-1]

# 頂点番号の振り直し
reorder = [None] * N
for i in range(N):
    reorder[order[i]] = i

for i in range(N):
    res = -1
    ans = -1
    for v in Graph2[i]:
        if res < reorder[v]:
            res = reorder[v]
            ans = v
    print(ans+1)
