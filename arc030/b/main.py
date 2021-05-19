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
    n, x = map(int, input().split())
    h = list(map(int, input().split()))
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(lambda x: int(x)-1, input().split())
        adj[a].append(b)
        adj[b].append(a)
    # print(adj)

    queue = deque([x-1])
    parent = [-2] * n
    parent[x-1] = -1

    while queue:
        now = queue.popleft()
        for u in adj[now]:
            if parent[u] == -2:
                queue.append(u)
                parent[u] = now
        # print(parent)
    ans = 0
    used = [True] * n
    for i in range(n):
        if h[i] == 1:
            now = i
            while used[now] and parent[now] != -1:
                ans += 2
                used[now] = False
                now = parent[now]
    print(ans)


if __name__ == "__main__":
    main()
