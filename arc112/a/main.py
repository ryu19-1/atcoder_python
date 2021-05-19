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
    T = int(input())
    for _ in range(T):
        L, R = map(int, input().split())
        if R-L < L:
            print(0)
        else:
            ans = (R - 2*L+1) * (R - 2*L+2) // 2
            print(ans)


if __name__ == "__main__":
    main()
