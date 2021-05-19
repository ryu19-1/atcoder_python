#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


N = int(input())
z = [None] * N
w = [None] * N
for i in range(N):
    x, y = map(int, input().split())
    z[i] = x + y
    w[i] = x - y

print(max(max(z)-min(z), max(w)-min(w)))
