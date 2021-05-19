#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate
from math import gcd

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def extgcd(a, b):
    global x, y
    if b == 0:
        return a
    else:
        tmpg = extgcd(b, a % b)
        x, y = y, x - (a // b)*y
        # print(a, b, x, y)
        return tmpg


T = int(input())
for _ in range(T):
    N, S, K = map(int, input().split())
    # 拡張Euqlid互除法
    x = 1
    y = 0
    g = extgcd(K, N)
    if S % g != 0:
        print(-1)
    else:
        N //= g
        S //= g
        K //= g
        print(x*(-S) % N)
