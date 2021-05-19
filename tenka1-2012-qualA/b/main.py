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
    c = input().split(' ')
    # print(c)
    ans = ''
    for cc in c:
        if cc != '':
            ans += ',' + cc
    print(ans[1:])


if __name__ == "__main__":
    main()
