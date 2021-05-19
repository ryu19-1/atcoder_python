#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def LCS(s, t):
    N = len(s)
    M = len(t)
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N - 1, -1, -1):
        for j in range(M - 1, -1, -1):
            r = max(dp[i + 1][j], dp[i][j + 1])
            if s[i] == t[j]:
                r = max(r, dp[i+1][j+1] + 1)
            dp[i][j] = r
    return dp[0][0]


def main():
    N = int(input())
    S = input()
    ans = N
    for i in range(N):
        for j in range(i + 1, N):
            if S[i] == S[j]:
                res = LCS(S[i:j], S[j:N])
                ans = min(ans, N - 2 * res)
    print(ans)


if __name__ == "__main__":
    main()
