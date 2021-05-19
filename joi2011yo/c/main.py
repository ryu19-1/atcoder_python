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
    K = int(input())
    for _ in range(K):
        # 0:Red, 1:Blue, 2:Yellow
        x, y = map(lambda x: int(x) - 1, input().split())
        x = min(x, N - x-1)
        y = min(y, N - y-1)
        if y <= x:
            print(y % 3 + 1)
        else:
            print(x % 3 + 1)


if __name__ == "__main__":
    main()
