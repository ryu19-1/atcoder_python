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
    check = set()
    for i in range(2, 10 ** 5 + 1):
        now = i*i
        while now <= 10 ** 10:
            check.add(now)
            now *= i
    check = sorted(check)
    N = int(input())
    # print(check)
    d = bisect_right(check, N)
    print(N-d)


if __name__ == "__main__":
    main()
