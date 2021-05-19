#!/usr/bin/env python3
N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())
ans = 10**12
# 方針：普通の食事X回、質素な食事Y回で探索する
for x in range(N+1):
    y = ((N-x)*E - B*x - H)//(D+E) + 1
    if 0 <= y <= N-x:
        ans = min(ans,A*x+C*y)
    elif y < 0:
        ans = min(ans,A*x)
print(ans)