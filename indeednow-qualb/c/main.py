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
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        adj[a].append(b)
        adj[b].append(a)

    q = []
    heappush(q, 0)
    visit = [-1] * N
    visit[0] = 1
    ans = []

    while len(q) > 0:
        now = heappop(q)
        ans.append(now + 1)
        # print(now, adj[now])
        for u in adj[now]:
            if visit[u] < 0:
                heappush(q, u)
                visit[u] = 1
    print(*ans)


if __name__ == "__main__":
    main()
