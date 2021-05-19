#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def dfs(u,adj):
    if len(adj[u]) == 0:
        return 1
    else:
        tmp = [dfs(v,adj) for v in adj[u]]
        return max(tmp) + min(tmp) + 1


def main():
    N = int(input())
    B = [int(input()) for _ in range(N-1)]
    adj = [[] for _ in range(N)]
    for i,b in enumerate(B):
        adj[b-1].append(i+1)
    print(dfs(0,adj))

if __name__ == "__main__":
    main()
