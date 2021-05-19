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
    for _ in range(M):
        u, v, c = map(lambda x: int(x) - 1, input().split())
        adj[u].append((v, c))
        adj[v].append((u, c))

    queue = deque([0])
    visit = [-1] * N
    visit[0] = 0

    while queue:
        now = queue.popleft()
        for u, label in adj[now]:
            if visit[u] < 0:
                queue.append(u)
                if visit[now] != label:
                    visit[u] = label
                else:
                    visit[u] = (label + 1) % N

    [print(a+1) for a in visit]


if __name__ == "__main__":
    main()
