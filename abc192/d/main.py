#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7

# x進数がM以下か調べる


def check(n):
    if n < d + 1 or M < n:
        return False
    res = 0
    for i in range(L):
        res += int(X[L - 1 - i]) * pow(n, i)
    # print(n, res)
    if res <= M:
        return True
    else:
        return False


X = input()
L = len(X)
d = max([int(x) for x in X])
# print(d)
M = int(input())
if L == 1:
    if int(X) <= M:
        print(1)
    else:
        print(0)
    exit()

l = d  # ちゃんと範囲外
r = M+1  # ちゃんと範囲外
while abs(r - l) > 1:  # 逆転もありうる
    mid = (r + l) // 2
    if check(mid):
        l = mid
    else:
        r = mid

print(l-d)
