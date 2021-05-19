#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    N, M, X, Y = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        A, B, T, K = map(int, input().split())
        adj[A-1].append((B-1, T, K))
        adj[B - 1].append((A - 1, T, K))

    INF = 10**24
    q = [(0, X-1)]  # 始点のコストとindex
    d = [INF] * N
    d[X-1] = 0

    while len(q) > 0:
        cost, u = heappop(q)
        if cost > d[u]:
            continue
        for v, t, k in adj[u]:
            tmp = (d[u]+k-1)//k * k + t  # かかる時間
            if tmp < d[v]:
                d[v] = tmp
                heappush(q, (d[v], v))
    if d[Y - 1] == INF:
        print(-1)
    else:
        print(d[Y-1])


if __name__ == "__main__":
    main()
