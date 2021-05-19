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
    L = int(input())
    A = [0]*L
    for i in range(L - 1):
        B = int(input())
        A[i+1] = A[i] ^ B
    BL = int(input())
    if A[0] != A[-1] ^ BL:
        print(-1)
    else:
        [print(a) for a in A]


if __name__ == "__main__":
    main()
