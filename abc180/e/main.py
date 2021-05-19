#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10**12


def DFS(s, v):
    if dp[s][v] >= 0:
        return dp[s][v]
    if s == (1 << N) - 1 and v == 0:
        return dp[s][v]

    res = INF
    for u in range(N):
        if not (s >> u & 1):
            res = min(res, DFS(s | 1 << u, u) + dist[v][u])

    dp[s][v] = res
    return res


N = int(input())
xyz = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * N for _ in range(1 << N)]
dist = [[INF] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        dist[i][j] = abs(xyz[j][0]-xyz[i][0]) + abs(xyz[j]
                                                    [1] - xyz[i][1]) + max(0, xyz[j][2] - xyz[i][2])
# print(dist)
ans = DFS(0, 0)
print(ans+1)
