#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def judge(i, j):
    if memo[i][j] != -1:
        return memo[i][j]
    # 下、右、右下が全部勝ちなら負け、それ以外なら「意図的に」負けるを選ぶように遷移するから勝てる
    res = 0
    dx = [1, 0, 1]
    dy = [0, 1, 1]
    for k in range(3):
        y = i + dy[k]
        x = j + dx[k]
        if 0 <= y < H and 0 <= x < W and S[y][x] == '.':
            if judge(y, x) == 0:
                res = 1
    memo[i][j] = res
    return res


H, W = map(int, input().split())
S = [input() for _ in range(H)]
memo = [[-1] * W for _ in range(H)]  # -1: 未定, 0: 負け, 1: 勝ち

ans = judge(0, 0)
print(['Second', 'First'][ans])
# print(memo)
