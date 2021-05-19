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
    a, b, c, d = map(int, input().split())
    print(max([a*c, a*d, b*c, b*d]))


if __name__ == "__main__":
    main()
