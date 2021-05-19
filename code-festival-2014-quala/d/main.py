#!/usr/bin/env python3
INF = 10**18

A, K = map(int, input().split())
B = '0'+str(A)
N = len(B)
ans = INF
for r in range(N-1):
    for i in range(10):
        for j in range(10):
            res = B[:r] + str(i) + str(j) * (N - r - 1)
            # print(res, str(int(res)))
            res = str(int(res))
            if len({*res}) <= K:
                ans = min(ans, abs(A - int(res)))
print(ans)
