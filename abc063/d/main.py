#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7

N, A, B = map(int, input().split())
h = [int(input()) for _ in range(N)]


def ok(m):
    t = h[:]
    for i in range(N):
        t[i] = max(0, t[i]-B*m)
    res = 0
    # print(t)
    for i in range(N):
        res += (t[i]+A-B-1)//(A-B)
    if res <= m:
        return True
    else:
        return False


def main():
    l = 0
    r = 10 ** 9
    while r - l > 1:
        m = (l + r) // 2
        if ok(m):
            r = m
        else:
            l = m
        # print(l, r)
    print(r)


if __name__ == "__main__":
    main()
