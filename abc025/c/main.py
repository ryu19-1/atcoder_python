#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7

def cal_score(s):
    n = sum([s[i].count(0) for i in range(3)])
    if n == 0:# scoreを計算
        score = 0
        for i in range(2):
            for j in range(3):
                if s[i][j] == s[i+1][j]:
                    score += b[i][j]

        for i in range(3):
            for j in range(2):
                if s[i][j] == s[i][j+1]:
                    score += c[i][j]
        return score
    else:
        # 置ける場所に全部置いてスコアを計算し、手番によって最大値or最小値を返す
        candidate = []
        for i in range(3):
            for j in range(3):
                if s[i][j] == 0:
                    s[i][j] = (n % 2)+1
                    candidate.append(cal_score(s))
                    s[i][j] = 0
        
        if n % 2 == 1:
            return max(candidate)
        else:
            return min(candidate)

total = 0
b = [None] * 2
for i in range(2):
    b[i] = list(map(int, input().split()))
    total += sum(b[i])

c = [None] * 3
for i in range(3):
    c[i] = list(map(int, input().split()))
    total += sum(c[i])

s = [[0]*3 for _ in range(3)]# 盤面を保存
ans = cal_score(s)
print(ans)
print(total-ans)