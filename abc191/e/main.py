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

    adj = [[] for _ in range(N)]
    adj2 = [[] for _ in range(N)]  # adj2[i]: iへ行ける町のリスト
    for _ in range(M):
        A, B, C = map(int, input().split())
        A -= 1
        B -= 1
        adj[A].append((C, B))
        adj2[B].append((C, A))

    for i in range(N):
        q = [(0, i)]  # 始点のコストとindex
        d = [INF] * N
        d[i] = 0

        while len(q) > 0:
            cost, u = heappop(q)
            if cost > d[u]:
                continue
            for c, v in adj[u]:
                tmp = d[u] + c
                if tmp < d[v]:
                    d[v] = tmp
                    heappush(q, (d[v], v))
        res = INF
        for c, v in adj2[i]:
            res = min(res, d[v] + c)
        if res == INF:
            print(-1)
        else:
            print(res)


if __name__ == "__main__":
    main()
