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
    ans = INF
    for i in range(N):
        A, P, X = map(int, input().split())
        if X - A > 0:
            ans = min(ans, P)
    if ans == INF:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
