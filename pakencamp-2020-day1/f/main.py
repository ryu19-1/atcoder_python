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
    P = int(input())
    if P == 1:
        print(1)
    else:
        F = [1, 1]
        while F[-1] > 0:
            F.append((F[-1]+F[-2]) % P)
        print(len(F))

if __name__ == "__main__":
    main()
