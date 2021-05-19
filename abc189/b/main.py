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
    N, X = map(int, input().split())
    now = 0
    ans = -1
    for i in range(N):
        V, P = map(int, input().split())
        now += V * P
        if now > 100 * X:
            ans = i + 1
            break
    print(ans)


if __name__ == "__main__":
    main()
