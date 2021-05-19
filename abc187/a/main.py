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
    A, B = input().split()
    print(max(int(A[0])+int(A[1])+int(A[2]), int(B[0])+int(B[1])+int(B[2])))


if __name__ == "__main__":
    main()
