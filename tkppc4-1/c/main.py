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
    for M in range(2, 11):
        res = []
        tmp = N
        while tmp > 0:
            res.append(str(tmp % M))
            tmp //= M
        # print(res)
        if ''.join(res[::-1]) == str(X):
            print(M)
            exit()


if __name__ == "__main__":
    main()
