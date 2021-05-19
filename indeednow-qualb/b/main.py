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
    t = input()
    if len(s) != len(t):
        print(-1)
        exit()
    N = len(s)
    ans = 0
    while ans < N:
        if s == t:
            print(ans)
            exit()
        s = s[-1] + s[:-1]
        ans += 1
    print(-1)


if __name__ == "__main__":
    main()
