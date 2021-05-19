#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


N = int(input())
adj = [[] for _ in range(N)]
a = [None] * N
b = [None] * N
for i in range(N - 1):
    aa, bb = map(lambda x: int(x) - 1, input().split())
    a[i] = aa
    b[i] = bb
    adj[aa].append(bb)
    adj[bb].append(aa)

queue = deque([0])
parent = [None] * N
parent[0] = -1

while queue:
    now = queue.popleft()
    for u in adj[now]:
        if parent[u] is None:
            queue.append(u)
            parent[u] = now
# print(parent)

dp = [0] * N
Q = int(input())
for _ in range(Q):
    t, e, x = map(int, input().split())
    e -= 1
    if t == 1:
        ae = a[e]
        be = b[e]
    else:
        ae = b[e]
        be = a[e]
    if parent[ae] == be:
        dp[ae] += x
    else:
        dp[0] += x
        dp[be] -= x

ans = [0] * N
ans[0] = dp[0]
# print(ans)

queue = deque([0])
visit = [-1] * N
visit[0] = 0

while queue:
    now = queue.popleft()
    visit[now] = 0
    for u in adj[now]:
        if visit[u] < 0:
            queue.append(u)
            ans[u] += dp[u]+ans[now]
    # print(now, ans)
[print(ans[i]) for i in range(N)]
