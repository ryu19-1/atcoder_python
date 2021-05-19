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
    if S == 'RRR':
        print(3)
    elif 'RR' in S:
        print(2)
    elif 'R' in S:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()
