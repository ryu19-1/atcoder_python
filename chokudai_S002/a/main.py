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
    AB = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        print(AB[i][0]*AB[i][1])


if __name__ == "__main__":
    main()
