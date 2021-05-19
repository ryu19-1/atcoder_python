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
    H, W, N, M = map(int, input().split())
    S = [[0] * W for _ in range(H)]  # 電球1, ブロック2
    for _ in range(N):
        a, b = map(lambda x: int(x) - 1, input().split())
        S[a][b] = 1
    for _ in range(M):
        c, d = map(lambda x: int(x) - 1, input().split())
        S[c][d] = 2
    # AB = [list(map(lambda x: int(x)-1, input().split())) for _ in range(N)]
    # CD = [list(map(lambda x:int(x) - 1, input().split())) for _ in range(M)]
    # print(S)
    dp = [[0]*(H*W) for _ in range(4)]
    dy = [0, -1, 0, 1]
    dx = [-1, 0, 1, 0]

    for i in range(H):
        for j in range(W):
            # if S[i][j] == 1:
            #     dp[k][W * i + j] = 1
            #     continue
            if S[i][j] == 2:
                continue
            for k in range(2):
                y = i + dy[k]
                x = j + dx[k]
                if S[i][j] == 1:
                    dp[k][W*i+j] = 1
                elif 0 <= y < H and 0 <= x < W and dp[k][W*y+x] > 0:
                    dp[k][W * i + j] = dp[k][W * y + x] + 1

    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            if S[i][j] == 2:
                continue
            for k in range(2):
                y = i + dy[k+2]
                x = j + dx[k + 2]
                if S[i][j] == 1:
                    dp[k+2][W*i+j] = 1
                elif 0 <= y < H and 0 <= x < W and dp[k+2][W*y+x] > 0:
                    dp[k + 2][W * i + j] = dp[k + 2][W * y + x] + 1

        # print(i, dp[3])

    # for i in range(4):
    #     print(dp[i])
    ans = H*W-M
    for i in range(H):
        for j in range(W):
            if S[i][j] != 0:
                continue
            cnt = 0
            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]
                if 0 <= y < H and 0 <= x < W and S[y][x] != 2:
                    cnt += dp[k][W * y + x]
            # print(i, j, cnt)
            if cnt == 0:
                ans -= 1
                # print(i, j)
    print(ans)


if __name__ == "__main__":
    main()
