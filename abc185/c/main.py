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
    # L-1C11
    ans = 1
    for i in range(11):
        ans *= L - 1 - i
        ans //= i + 1
    print(ans)


if __name__ == "__main__":
    main()
