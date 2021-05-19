#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right


N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (1 << N)
flag = [0] * (1 << N)

# print(a)


def f(S):
    # print(S)
    if flag[S]:
        return dp[S]
    else:
        flag[S] = 1
        tmp = 0
        for i in range(N):
            for j in range(i + 1, N):
                if (1 << i & S) and (1 << j & S):
                    tmp += a[i][j]
        T = (S - 1) & S
        # print(S, (S - 1) & S)
        while T > 0:
            tmp = max(tmp, f(T) + f(S ^ T))
            T = (T - 1) & S
            # print(T)
        dp[S] = tmp
        return dp[S]


print(f((1 << N) - 1))
# print(dp)
