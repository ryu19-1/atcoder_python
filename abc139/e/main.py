#!/usr/bin/env python3
import sys

sys.setrecursionlimit(10**6)


def dfs(v):
    if visited[v]:
        if not calc[v]:
            return -1
        return dp[v]
    else:
        visited[v] = True
        for u in Graph[v]:
            res = dfs(u)
            if res == -1:
                return -1
            dp[v] = max(dp[v], res + 1)
        calc[v] = True
        return dp[v]


N = int(input())
# i vs jの試合を辞書順に番号にする
check = [[None] * N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        check[i][j] = cnt
        check[j][i] = cnt
        cnt += 1
# print(check)
Graph = [[] for _ in range(cnt)]
for i in range(N):
    A = list(map(lambda x: int(x) - 1, input().split()))
    now = check[i][A[0]]
    for j in range(1, N-1):
        nex = check[i][A[j]]
        # print(now, nex)
        Graph[now].append(nex)
        now = nex
# print(Graph)


visited = [False] * cnt
calc = [False] * cnt
dp = [1] * cnt


ans = 0
for i in range(cnt):
    res = dfs(i)
    if res == -1:
        print(-1)
        exit()
    ans = max(ans, res)
print(ans)
