#!/usr/bin/env python3
from heapq import heappop, heappush

N, K = map(int, input().split())
q = []
for _ in range(N):
    t, d = map(int, input().split())
    heappush(q, (-d, t-1))

ans = 0
now = [[] for _ in range(N)]
used = set()
for _ in range(K):
    d, t = heappop(q)
    d = -d
    ans += d
    heappush(now[t], d)
    used.add(t)

removeCandidate = []
for i in range(N):
    while len(now[i]) > 1:
        d = heappop(now[i])
        heappush(removeCandidate, d)

x = len(used)
ANS = ans + x * x
res = ans
for p in range(x + 1, N + 1):
    if len(removeCandidate) == 0:
        print(ANS)
        exit()
    d = heappop(removeCandidate)
    res -= d
    while True:
        if len(q) == 0:
            print(ANS)
            exit()
        d, t = heappop(q)
        if t in used:
            continue
        d = -d
        res += d
        ANS = max(ANS, res + p * p)
        used.add(t)
        break
print(ANS)
