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
    N = int(input())
    dp = [1, 1]  # True, Falseの個数
    for i in range(N):
        S = input()
        nextdp = [0, 0]
        if S == 'AND':
            nextdp = [dp[0], dp[0] + 2 * dp[1]]
        else:
            nextdp = [dp[0]*2+dp[1], dp[1]]
        dp = nextdp[:]
    print(dp[0])


if __name__ == "__main__":
    main()
