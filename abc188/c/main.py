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
    N = int(input())
    A = list(map(int, input().split()))
    pmax = max(A[:2 ** (N - 1)])
    qmax = max(A[2**(N-1):])
    p = A.index(pmax)
    q = A.index(qmax)
    if pmax < qmax:
        print(p+1)
    else:
        print(q+1)


if __name__ == "__main__":
    main()
