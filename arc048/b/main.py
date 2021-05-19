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
    RH = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * 100001 for _ in range(3)]
    for i in range(N):
        dp[RH[i][1] % 3][RH[i][0]] += 1

    for i in range(3):
        for j in range(100000):
            dp[i][j + 1] += dp[i][j]
    # print(dp)
    for i in range(N):
        # print(i, RH[i])
        win = 0
        draw = dp[RH[i][1] % 3][RH[i][0]]-dp[RH[i][1] % 3][RH[i][0]-1]-1
        # R+1以上の累積和
        for j in range(3):
            win += dp[j][100000] - dp[j][RH[i][0]]
        win += dp[(RH[i][1] - 1) % 3][RH[i][0]] - \
            dp[(RH[i][1] - 1) % 3][RH[i][0] - 1]
        print(N-1-win-draw, win, draw)


if __name__ == "__main__":
    main()
