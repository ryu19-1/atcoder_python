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
    a, b, x, y = map(int, input().split())
    a -= 1
    b -= 1
    adj = [[] for _ in range(200)]
    for i in range(100):
        adj[i].append((x, 100+i))
        adj[100 + i].append((x, i))

    for i in range(99):
        adj[i+1].append((x, 100+i))
        adj[100 + i].append((x, i + 1))
        adj[i].append((y, i+1))
        adj[i+1].append((y, i))
        adj[i+100].append((y, i+101))
        adj[i+101].append((y, i + 100))

    INF = 10**12
    q = [(0, a)]  # 始点のコストとindex
    d = [INF] * 200
    d[a] = 0

    while len(q) > 0:
        cost, u = heappop(q)
        if d[u] < cost:
            continue
        for c, v in adj[u]:
            tmp = d[u] + c
            if tmp < d[v]:
                d[v] = tmp
                heappush(q, (d[v], v))

    print(d[b+100])


if __name__ == "__main__":
    main()
