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
    S = input()
    N = len(S)
    dp = [[0]*2 for _ in range(N+1)]  # flag: 0繰り上がりなし, 1繰り上がりあり
    for i in range(1, N + 1):

        s = int(S[N-i])
        # dp[i][0] = min(dp[i - 1][0] + s, dp[i - 1][1] + s + 1)
        dp[i][0] = dp[i - 1][0] + s
        if s < 9:
            dp[i][0] = min(dp[i][0], dp[i-1][1] + s + 1)

        dp[i][1] = dp[i - 1][0] + (10 - s)
        if dp[i - 1][1] > 0:
            dp[i][1] = min(dp[i][1], dp[i-1][1]+(9-s))
        # dp[i][1] += dp[i - 1][0] + (10 - s)
        # if dp[i-1][1] > 0:
        #     dp[i][1] += dp[i-1][1] + s
        #     dp[i][1] += dp[i-1][1] + (9 - s)
        # print(i, s, dp)
    print(min(dp[N][0], dp[N][1]+1))


if __name__ == "__main__":
    main()
