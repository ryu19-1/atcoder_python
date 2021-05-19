#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
import sys
sys.setrecursionlimit(10**6)

# 入力
N = int(input())
adj = [[] for _ in range(N)]
ans = [None] * N

# グラフ探索で解いてみる
# c: 頂点vの色(0or1)
def dfs(v,parent,c):
    ans[v] = c
    for u,w in adj[v]:
        if u == parent:
            continue
        dfs(u,v,1-c) if w & 1 else dfs(u,v,c)

def main():
    for i in range(N-1):
        u, v, w = map(int, input().split())
        adj[u-1].append((v-1,w))
        adj[v-1].append((u-1,w))
    
    dfs(0,-1,1)
    [print(v) for v in ans]

if __name__ == "__main__":
    main()
