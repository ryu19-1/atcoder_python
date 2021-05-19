#!/usr/bin/env python3
from itertools import accumulate

N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
INF = 10**18
ans = - INF
used = [0] * N
candidate = []

for i in range(N):
    if used[i]: continue
    now = i
    used[i] = 1
    tmp = [i]
    
    while P[now]-1 not in tmp:
        used[P[now]-1] = 1
        tmp.append(P[now]-1)
        now = P[now]-1

    candidate.append(tmp)

for tmp in candidate:
    M = len(tmp)
    accumT = []
    for t in tmp:
        accumT.append(C[t])
    loop = 3
    accumT = [0] + list(accumulate(accumT*loop))
    res = - INF

    if K <= M:
        for i in range(loop*M+1):
            for j in range(i+1,loop*M+1):
                if j-i > K:
                    break
                res = max(res,accumT[j]-accumT[i])
        ans = max(ans,res)
    else:
        SUM = accumT[M]
        if SUM > 0:
            addition = SUM * (K//M - 1)# K//M回回らない方がいい場合がある
            for i in range(loop*M+1):
                for j in range(i+1,loop*M+1):
                    if j-i > K%M+M:
                        break
                    res = max(res,accumT[j]-accumT[i])
            ans = max(ans,res+addition)
        else:
            for i in range(loop*M+1):
                for j in range(i+1,loop*M+1):
                    if j-i > M:
                        break
                    res = max(res,accumT[j]-accumT[i])
            ans = max(ans,res)
print(ans)