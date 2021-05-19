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
    N, M, L = map(int, input().split())
    adj = [[INF] * N for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        if C > L:
            # Lより長い辺はあっても意味ない
            continue
        adj[A-1][B-1] = C
        adj[B-1][A-1] = C

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
    # print(adj)
    adj2 = [[INF] * N for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            if adj[i][j] <= L:
                adj2[i][j] = 1
                adj2[j][i] = 1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                adj2[i][j] = min(adj2[i][j], adj2[i][k] + adj2[k][j])
    # print(adj2)
    Q = int(input())
    for _ in range(Q):
        s, t = map(int, input().split())
        if adj2[s - 1][t - 1] == INF:
            print(-1)
        else:
            print(adj2[s-1][t-1]-1)


if __name__ == "__main__":
    main()
