#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
import sys
sys.setrecursionlimit(10**6)


def DFS(v, parent):
    # print(v)
    res = 1
    for u in adj[v]:
        if u != parent:
            DFS(u, v)
            res *= (dp[u]+1) % M
            res %= M
    # if parent != -1:
    dp[v] = res
    # print(v, dp)


N, M = map(int, input().split())
adj = [[] for _ in range(N)]
for _ in range(N - 1):
    x, y = map(lambda x: int(x)-1, input().split())
    adj[x].append(y)
    adj[y].append(x)

# 頂点0(0-index)を始点とした木DPをDFSで解く
# dp[v]= 頂点vを根とする部分木について対応する部分木の値
dp = [-1] * N
DFS(0, -1)

print(dp)
# 頂点0からBFSで全頂点を辿り、都度dpの計算を行う
ans = [-1] * N
ans[0] = dp[0]


queue = deque([0])
visited = [1] * N
visited[0] = 0

while queue:
    now = queue.pop()
    d = len(adj[now])
    # 左累積
    cumL = [dp[u] for u in adj[now]]
    for i in range(d - 1):
        cumL[i + 1] *= cumL[i]
        cumL[i + 1] %= M
    # 右累積
    cumR = [dp[u] for u in adj[now]]
    for i in range(d - 2, -1, -1):
        cumR[i] *= cumR[i+1]
        cumR[i] %= M
    cnt = 0
    for u in adj[now]:
        if visited[u]:
            res = 1
            if cnt > 0:
                res *= cumL[cnt - 1]
            if cnt < d-1:
                res *= cumR[cnt + 1]
            ans[u] = res % M
            print(u, ans)
            queue.append(u)
            visited[u] = 0
        cnt += 1
print(dp)
print(ans)
# for i in range(N):
#     ans = 1
#     for k in dp[i]:
#         ans *= k
#         ans %= M
#     print((ans-1) % M)
