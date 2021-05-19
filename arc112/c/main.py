#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def DFS(v, turn):
    if dp[turn][v] != -1:
        return dp[turn][v]
    else:
        arr = []
        for u in adj[v]:
            arr.append(DFS(u, turn))
        if len(arr) == 0:
            dp[turn][v] = 1
            dp[1 - turn][v] = 0
        elif len(arr) == 1:
            dp[turn][v] = dp[turn][arr[0]] + 1
            dp[1-turn][v] = dp[1-turn][arr[0]]
        else:
            arr.sort()
            res = sum(arr[::2])
            res2 = sum(arr[1::2])
            dp[turn][v] = res2 + 1
            dp[1-turn][v] = res
        return dp[turn][v]


N = int(input())
parent = [0] + list(map(lambda x: int(x) - 1, input().split()))
adj = [[] for _ in range(N)]
for i in range(1, N):
    adj[parent[i]].append(i)
# print(adj)
dp = [[-1] * N for _ in range(2)]
print(DFS(0, 0))
print(dp)
