#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def DFS(v, p):
    res = 1
    for u in adj[v]:
        if u != p:
            res += DFS(u, v)
            parent[u] = v
    dp[v] = res
    return res


def calc(n):
    if memo[n - 1] > -1:
        return memo[n - 1]
    else:
        memo[n-1] = pow(pow(2, n, m), m-2, m)
        return memo[n-1]


N = int(input())
adj = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    adj[a].append(b)
    adj[b].append(a)

# dp[i]:= iを頂点とする部分木の要素数
dp = [0] * N
memo = [-1] * N
parent = [-1] * N
DFS(0, -1)
ans = 0
for i in range(N):
    L = len(adj[i])
    if L == 1:
        continue
    # つながっている頂点の部分技が全部白か１つだけ黒ならだめ
    # 左累積mergeと右累積mergeをとる
    values = []
    for j in adj[i]:
        if j == parent[i]:
            values.append(calc(dp[0] - dp[i]))
        else:
            values.append(calc(dp[j]))

    lcum = [1]
    for j in range(L):
        lcum.append(lcum[-1] * values[j] % m)
    rcum = [1]
    for j in range(L-1, -1, -1):
        rcum.append(rcum[-1] * values[j] % m)
    rcum = rcum[::-1]
    # 全部白のパターン
    res = lcum[-1]
    for j in range(L):
        # j番目だけ黒があり他は白だけ
        res += (lcum[j] * (1 - values[j]) % m) * rcum[j+1] % m
    res %= m
    ans += ((1-res) % m) * 500000004 % m
print(ans % m)
