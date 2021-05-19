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
    V, T, S, D = map(int, input().split())
    if T * V <= D <= S * V:
        print('No')
    else:
        print('Yes')


if __name__ == "__main__":
    main()
