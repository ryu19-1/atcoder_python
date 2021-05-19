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
    s = input()
    LIM = 8000
    x, y = map(int, input().split())
    x -= (len(s)-len(s.lstrip('F')))
    sl = s.lstrip('F').split('T')
    L = len(sl)
    # print(x, y, sl)
    xs = set()
    xs.add(x)
    for i in range(0, L, 2):
        nextxs = set()
        tmp = len(sl[i])
        for xx in xs:
            if abs(xx + tmp) <= LIM:
                nextxs.add(xx + tmp)
            if abs(xx - tmp) <= LIM:
                nextxs.add(xx - tmp)
        xs = nextxs.copy()

    ys = set()
    ys.add(y)
    for i in range(1, L, 2):
        nextys = set()
        tmp = len(sl[i])
        for yy in ys:
            if abs(yy + tmp) <= LIM:
                nextys.add(yy + tmp)
            if abs(yy - tmp) <= LIM:
                nextys.add(yy - tmp)
        ys = nextys.copy()

    if 0 in xs and 0 in ys:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
