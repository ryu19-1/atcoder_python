#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right


N, M = map(int, input().split())
A = [None] * M
B = [None] * M
adj = [set() for _ in range(N)]
for i in range(M):
    A[i], B[i] = map(lambda x: int(x) - 1, input().split())
    adj[A[i]].add(B[i])
    adj[B[i]].add(A[i])
dp = [N] * (1 << N)
flag = [0] * (1 << N)


def f(S):
    # print(S)
    if flag[S]:
        return dp[S]
    else:
        flag[S] = 1
        tmp = N
        check = True
        # S内の任意の頂点が2点で結ばれるか調べる
        for i in range(N):
            for j in range(i + 1, N):
                if (1 << i & S) and (1 << j & S):
                    if j not in adj[i]:
                        check = False
                        break
            if check == False:
                break
        if check:
            tmp = min(tmp, 1)

        T = (S - 1) & S
        # print(S, (S - 1) & S)
        while T > 0:
            tmp = min(tmp, f(T) + f(S ^ T))
            T = (T - 1) & S
            # print(T)
        dp[S] = tmp
        return dp[S]


print(f((1 << N) - 1))
# print(dp)
