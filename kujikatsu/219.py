#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 998244353


def main():
    N = int(input())
    ab = []
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        ab.append([a-1, b-1])
        adj[a-1].append(b-1)
        adj[b - 1].append(a - 1)

    parent = [None] * N
    parent[0] = 0

    queue = deque([0])

    while queue:
        now = queue.popleft()
        for u in adj[now]:
            if parent[u] is None:
                queue.append(u)
                parent[u] = now

    Q = int(input())
    scores = [0] * N
    for _ in range(Q):
        t, e, x = map(int, input().split())
        ae = ab[e - 1][0]
        be = ab[e - 1][1]
        if t == 2:
            ae, be = be, ae

        if parent[ae] == be:
            scores[ae] += x
        else:
            scores[0] += x
            scores[be] -= x
        # print(scores)

    queue = deque([0])
    ans = [-1] * N
    ans[0] = scores[0]

    while queue:
        now = queue.popleft()
        for u in adj[now]:
            if ans[u] < 0:
                queue.append(u)
                ans[u] = ans[now] + scores[u]
    [print(a) for a in ans]


if __name__ == "__main__":
    main()
