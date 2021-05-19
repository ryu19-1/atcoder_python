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
    N, M = map(int, input().split())
    s, t = map(lambda x: int(x) - 1, input().split())

    adj = [[] for _ in range(N)]
    for _ in range(M):
        x, y, dd = map(int, input().split())
        adj[x-1].append((dd, y-1))
        adj[y-1].append((dd, x-1))
    INF = 10**12
    q = [(0, s)]  # 始点のコストとindex
    d = [INF] * N
    d[s] = 0

    while len(q) > 0:
        cost, u = heappop(q)
        if cost > d[u]:
            continue
        for c, v in adj[u]:
            tmp = d[u] + c
            if tmp < d[v]:
                d[v] = tmp
                heappush(q, (d[v], v))
    # print(d)
    q = [(0, t)]  # 始点のコストとindex
    d2 = [INF] * N
    d2[t] = 0

    while len(q) > 0:
        cost, u = heappop(q)
        if cost > d2[u]:
            continue
        for c, v in adj[u]:
            tmp = d2[u] + c
            if tmp < d2[v]:
                d2[v] = tmp
                heappush(q, (d2[v], v))
    # print(d2)
    for i in range(N):
        if d[i] == d2[i] and d[i] != INF:
            print(i + 1)
            exit()
    print(-1)


if __name__ == "__main__":
    main()
