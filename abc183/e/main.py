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
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # adj = [[] for _ in range(W*H)]
    dy = [0, -1, -1]
    dx = [-1, 0, -1]
    dp = [[0] * (H*W) for _ in range(4)]  # 左、上、左上の順
    dp[3][0] = 1

    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            for k in range(3):
                y = i + dy[k]
                x = j + dx[k]
                if 0 <= y < H and 0 <= x < W:
                    dp[k][W*i+j] = (dp[k][W*y+x]+dp[3][W*y+x]) % m
                    dp[3][W*i+j] += dp[k][W*i+j]
            dp[3][W*i+j] %= m
    print(dp[3][H*W-1])

    # for i in range(H - 1, -1, -1):
    #     for j in range(W - 1, -1, -1):
    #         if S[i][j] == '#':
    #             continue
    #         for k in range(4):
    #             y = i + dy[k+4]
    #             x = j + dx[k+4]
    #             if 0 <= y < H and 0 <= x < W:
    #                 if S[y][x] == '.':
    #                     dp[i][j] += dp[y][x]

    # print(dp[H-1][W-1])


if __name__ == "__main__":
    main()
