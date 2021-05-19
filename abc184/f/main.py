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
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + [*accumulate(A)]
    print(A)
    array = set()
    for l in range(1, N + 1):
        for r in range(l, N + 1):
            array.add(A[r] - A[l - 1])

    print(sorted(array))


if __name__ == "__main__":
    main()
