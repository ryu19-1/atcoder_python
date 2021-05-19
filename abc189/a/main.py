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
    C = input()
    if C[0] == C[1] == C[2]:
        print('Won')
    else:
        print('Lost')


if __name__ == "__main__":
    main()
