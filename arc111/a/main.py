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
    N, M = map(int, input().split())
    r = []
    # 繰り返し二乗法
    while N > 1:
        if N % 2 == 0:
            r.append(0)
            N //= 2
        else:
            r.append(1)
            N -= 1
    r = r[::-1]
    # print(r)
    dp1 = [10 // M, 10 % M]
    dp = dp1[:]
    for rr in r:
        # print(r, dp)
        if rr == 0:
            nextdp = [(dp[0]*dp[0]*M + 2*dp[0]*dp[1] +
                       dp[1] * dp[1] // M) % M, (dp[1] * dp[1] % M) % M]
        else:
            nextdp = [(dp[0]*dp1[0]*M + dp[0]*dp1[1] + dp[1]*dp1[0] +
                       dp[1] * dp1[1] // M) % M, (dp[1] * dp1[1] % M) % M]
        dp = nextdp[:]
    print(dp[0] % M)


if __name__ == "__main__":
    main()
