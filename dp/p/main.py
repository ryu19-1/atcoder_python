#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
import sys
sys.setrecursionlimit(10**6)

N = int(input())
adj = [[] for _ in range(N)]
dp = [[1] * 2 for _ in range(N)]
p = 10**9+7


def DFS(v, parent):
    for u in adj[v]:
        if u != parent:
            DFS(u, v)
            dp[v][0] *= (dp[u][0] + dp[u][1]) % p
            dp[v][0] %= p
            dp[v][1] *= dp[u][0]
            dp[v][1] %= p


def main():
    for _ in range(N - 1):
        x, y = map(lambda x: int(x)-1, input().split())
        adj[x].append(y)
        adj[y].append(x)
    DFS(0, -1)
    print((dp[0][0]+dp[0][1]) % p)


if __name__ == "__main__":
    main()
