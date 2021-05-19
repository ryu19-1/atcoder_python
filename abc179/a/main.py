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
    S = input()
    if S[-1] == 's':
        print(S + 'es')
    else:
        print(S+'s')


if __name__ == "__main__":
    main()