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
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    S = -1
    G = -1
    adj = [[] for _ in range(26)]
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    dic = {}
    for i in range(26):
        dic[alpha[i]] = i
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(H):
        for j in range(W):
            if a[i][j] == 'S':
                S = W * i + j
            elif a[i][j] == 'G':
                G = W * i + j
            elif a[i][j] == '#':
                continue
            elif a[i][j] != '.':
                adj[W*H + dic[a[i][j]]].append((0, W*i+j))
                adj[W*i+j].append((1, W*H + dic[a[i][j]]))

    INF = 10**12
    q = [(0, S)]  # 始点のコストとindex
    d = [INF] * (W*H+26)
    d[S] = 0

    while len(q) > 0:
        cost, u = heappop(q)
        if d[u] < cost:
            continue
        for k in range(4):
            y = u//W + dy[k]
            x = u % W + dx[k]
            if 0 <= y < H and 0 <= x < W and a[y][x] != '#':
                tmp = d[u] + 1
                v = W*y+x
                if tmp < d[v]:
                    d[v] = tmp
                    heappush(q, (d[v], v))
        for c, v in adj[u]:
            tmp = d[u] + c
            if tmp < d[v]:
                d[v] = tmp
                heappush(q, (d[v], v))

    # print(d)
    if d[G] == INF:
        print(-1)
    else:
        print(d[G])


if __name__ == "__main__":
    main()
