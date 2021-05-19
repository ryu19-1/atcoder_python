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
    X = list(map(int, input().split()))
    S = input()
    S = ['ABC'.index(S[i]) for i in range(N)]
    # print(S)
    Xcost = [[min(2*X[0], 2*X[1]), min(X[0], X[1]+X[2]), min(X[1], X[0]+X[2])],
             [min(X[0], X[1] + X[2]), min(2*X[0], 2*X[2]), min(X[2], X[1]+X[0])],
             [min(X[1], X[0]+X[2]), min(X[2], X[1]+X[0]), min(2*X[2], 2*X[1])]]

    adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        adj[a-1].append((b-1, c))
        adj[b-1].append((a-1, c))
    INF = 10 ** 12
    q = [(0, 0)]  # 始点のコストとindex
    d = [INF] * N
    d[0] = 0
    # print(d)
    for i in range(1, N):
        d[i] = min(d[i], Xcost[S[0]][S[i]])
    print(d)
    while len(q) > 0:
        cost, u = heappop(q)
        for v, c in adj[u]:
            tmp = d[u] + c
            if tmp < d[v]:
                d[v] = tmp
                heappush(q, (d[v], v))
    print(d)


if __name__ == "__main__":
    main()
