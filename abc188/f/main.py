#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def DFS(y):
    if y in memo:
        return memo[y]
    if y == 1:
        return abs(X-1)
    if y % 2 == 0:
        memo[y] = min(DFS(y // 2) + 1, abs(X - y))
        return memo[y]
    else:
        memo[y] = min([DFS(y + 1) + 1, DFS(y-1)+1, abs(X-y)])
        return memo[y]


X, Y = map(int, input().split())
if X >= Y:
    print(X - Y)
    exit()
memo = {}
print(DFS(Y))
