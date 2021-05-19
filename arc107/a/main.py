#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 998244353


def main():
    a, b, c = map(int, input().split())
    tmpa = (a * (a + 1) % m) * pow(2, m-2, m) % m
    tmpb = (b * (b + 1) % m) * pow(2, m-2, m) % m
    tmpc = (c * (c + 1) % m) * pow(2, m-2, m) % m
    ans = (tmpa * tmpb % m) * tmpc % m
    print(ans)


if __name__ == "__main__":
    main()
