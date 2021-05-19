#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
adj = [[] for _ in range(N)]

def rec(v,visited,order):
    visited[v] = 0
    for u in adj[v]:
        if visited[u] < 0:
            rec(u,visited,order)
    order.append(v)

def main():
    xy = []
    for _ in range(M):
        x, y = map(int, input().split())
        xy.append((x-1,y-1))
        adj[x-1].append(y-1)
    
    # トポロジカルソート（dfsによって実装）
    visited = [-1] * N
    order = []
    for i in range(N):
        if visited[i] < 0:
            rec(i,visited,order)

    # 自分を始点とするパスの最長を保存
    dp = [0]*(N+1)
    for o in order:
        for u in adj[o]:
            dp[o] = max(dp[o],dp[u]+1)
    
    print(max(dp))

if __name__ == "__main__":
    main()