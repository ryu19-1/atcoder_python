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
    C1, A = input().split()
    C2, B = input().split()

    if C1 == C2:
        print(abs(int(A) - int(B)) // 15)
    else:
        print(abs(int(A) + int(B)) // 15)


if __name__ == "__main__":
    main()
