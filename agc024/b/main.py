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
    P = [int(input()) for _ in range(N)]
    ans = INF

    desc = N
    for i in range(N - 1, -1, -1):
        if P[i] == desc:
            desc -= 1

    ans = min(ans, desc)
    print(ans)


if __name__ == "__main__":
    main()
