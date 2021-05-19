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
    X, Y = map(int, input().split())
    if X == 0 and Y == 0:
        print(1, 1)
    elif X == 0:
        print(Y * 2, Y)
    elif Y == 0:
        print(X, 2 * X)
    elif X == Y:
        print(-1)
    elif X > Y:
        print(X, X + Y)
    else:
        print(X+Y, Y)


if __name__ == "__main__":
    main()
