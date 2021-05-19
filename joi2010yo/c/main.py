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
    N = int(input())
    M = int(input())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x) - 1, input().split())
        adj[a].append(b)

    queue = deque([0])
    visit = [-1] * N
    visit[0] = 0

    while queue:
        now = queue.popleft()
        for u in adj[now]:
            if visit[u] < 0:
                queue.append(u)
                visit[u] = visit[now] + 1
    print(len([*filter(lambda x: 1 <= x <= 2, visit)]))


if __name__ == "__main__":
    main()
