#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

m = 10**9 + 7


def main():
    N, K = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        adj[a].append(b)
        adj[b].append(a)

    queue = deque([0])
    visit = [-1] * N
    visit[0] = 1
    ans = K

    while queue:
        now = queue.popleft()
        cnt = K - 1
        if now > 0:
            cnt -= 1
        for u in adj[now]:
            if visit[u] < 0:
                queue.append(u)
                visit[u] = 1
                ans *= cnt
                ans %= m
                cnt -= 1
    print(ans)


if __name__ == "__main__":
    main()
