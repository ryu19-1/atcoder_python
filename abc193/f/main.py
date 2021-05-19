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
    c = [input() for _ in range(N)]
    # Black: 0, White: 1
    dp = [[[0] * 2 for _ in range(N)] for _ in range(N)]
    prev = [0, 0]
    for i in range(N):
        for j in range(N):
            # res = prev[:]
            # 左マスがある時
            if j > 0:
                y = i
                x = j-1
                if c[i][j] == 'B':
                    if c[y][x] == 'W':
                        prev[0] = max(prev[0], prev[1]+1)
                    elif c[y][x] == '?':
                        prev[0] = max(prev[0], prev[1]+1)
                if c[i][j] == 'W':
                    if c[y][x] == 'B':
                        prev[1] = max(prev[1], prev[0]+1)
                    elif c[y][x] == '?':
                        prev[1] = max(prev[1], prev[0]+1)
                if c[i][j] == '?':
                    if c[y][x] == 'W':
                        prev[0] = max(prev[0], prev[1]+1)
                    elif c[y][x] == 'B':
                        prev[1] = max(prev[1], prev[0]+1)
                    else:
                        tmp = [max(prev[0], prev[1] + 1),
                               max(prev[0] + 1, prev[1])]
                        prev = tmp[:]
            print(prev)
            # 上マスがある時
            if i > 0:
                y = i-1
                x = j
                if c[i][j] == 'B':
                    if c[y][x] == 'W':
                        prev[0] = max(prev[0], prev[1]+1)
                    elif c[y][x] == '?':
                        prev[0] = max(prev[0], prev[1]+1)
                if c[i][j] == 'W':
                    if c[y][x] == 'B':
                        prev[1] = max(prev[1], prev[0]+1)
                    elif c[y][x] == '?':
                        prev[1] = max(prev[1], prev[0]+1)
                if c[i][j] == '?':
                    if c[y][x] == 'W':
                        prev[0] = max(prev[0], prev[1]+1)
                    elif c[y][x] == 'B':
                        prev[1] = max(prev[1], prev[0]+1)
                    else:
                        tmp = [max(prev[0], prev[1] + 1),
                               max(prev[0] + 1, prev[1])]
                        prev = tmp[:]
            dp[i][j] = prev[:]
            # prev = dp[i][j][:]
            print(i, j, prev)
    if c[N - 1][N - 1] == 'B':
        print(dp[N - 1][N - 1][0])
    elif c[N-1][N-1] == 'W':
        print(dp[N - 1][N - 1][1])
    else:
        print(max(dp[N - 1][N - 1]))
    print(dp)


if __name__ == "__main__":
    main()
