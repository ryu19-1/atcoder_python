#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


class UnionFind():
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.size[x] < self.size[y]:
                x, y = y, x
            self.parents[y] = x
            self.size[x] += self.size[y]


N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
C = list(map(int, input().split()))
adj = [[] for _ in range(N)]
uf = UnionFind(N)
for i in range(M):
    uf.union(AB[i][0] - 1, AB[i][1] - 1)
    adj[AB[i][0]-1].append(AB[i][1]-1)
    adj[AB[i][1]-1].append(AB[i][0]-1)

# 頂点Cの集合が連結か判定
for i in range(K-1):
    if uf.find(C[i] - 1) != uf.find(C[i + 1] - 1):
        print(-1)
        exit()

# Cそれぞれの距離を求める
visit = [[-1] * N for _ in range(K)]
for k in range(K):
    queue = deque([C[k]-1])
    visit[k][C[k]-1] = 0

    while queue:
        now = queue.popleft()
        for u in adj[now]:
            if visit[k][u] < 0:
                queue.append(u)
                visit[k][u] = visit[k][now] + 1

# bitDP(配るDP)
# dp[S][i]: 集合Sまで辿って最後がiの時の個数の最小値
dp = [[INF] * K for _ in range(1 << K)]
for i in range(K):
    dp[1 << i][i] = 1

for S in range(1 << K):
    for i in range(K):
        if dp[S][i] == INF:
            continue
        for j in range(K):
            # 訪問済み
            if S & (1 << j):
                continue
            dp[S | 1 << j][j] = min(
                dp[S ^ (1 << j)][j], dp[S][i]+visit[i][C[j]-1])


ans = min(dp[-1])
print(ans)
