#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def check(t):
    for i in range(N):
        for j in range(i + 1, N):
            if t / c[i] + t / c[j] < abs(x[i] - x[j]) or t / c[i] + t / c[j] < abs(y[i] - y[j]):
                return False
    return True


N = int(input())
x = [None] * N
y = [None] * N
c = [None] * N
for i in range(N):
    x[i], y[i], c[i] = map(int, input().split())

l = 0  # ちゃんと範囲外
r = 10 ** 19  # ちゃんと範囲外
while abs(r - l) > 10e-6:  # 逆転もありうる
    mid = (r + l) / 2
    if check(mid):
        r = mid
    else:
        l = mid
print(r)
