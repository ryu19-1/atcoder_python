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
    E = list(map(int, input().split()))
    B = int(input())
    L = list(map(int, input().split()))
    n = set(E) & set(L)
    # print(n)
    if len(n) == 6:
        print(1)
    elif len(n) == 5:
        if B in L:
            print(2)
        else:
            print(3)
    elif len(n) > 2:
        print(8-len(n))
    else:
        print(0)


if __name__ == "__main__":
    main()
