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
    # print(adj)
    c = list(map(int, input().split()))
    c.sort(reverse=True)

    queue = deque([0])
    visit = [-1] * N
    visit[0] = c.pop(0)
    ans = 0

    while queue:
        now = queue.popleft()
        for u in adj[now]:
            if visit[u] < 0:
                queue.append(u)
                visit[u] = c.pop(0)
                ans += min(visit[now], visit[u])
    print(ans)
    print(*visit)


if __name__ == "__main__":
    main()
