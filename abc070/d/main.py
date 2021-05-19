#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7

N = int(input())
adj = [[] for _ in range(N)]
rtree = [None] * N

def dfs(v,parent,dist):
    rtree[v] = dist
    for u, c in adj[v]:
        if u == parent:
            continue
        dfs(u,v,dist+c)

def main():
    for _ in range(N-1):
        a, b, c = map(int, input().split())
        adj[a-1].append((b-1,c))
        adj[b-1].append((a-1,c))
    Q, K = map(int, input().split())

    # Kを頂点とする根付き木を作成する
    dfs(K-1,-1,0)

    for _ in range(Q):
        x, y = map(lambda x: int(x)-1, input().split())
        print(rtree[x] + rtree[y])

if __name__ == "__main__":
    main()
