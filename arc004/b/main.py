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
    d = [int(input()) for _ in range(N)]
    ansmax = sum(d)
    # cumd = [0]
    # for i in range(N):
    #     cumd.append(cumd[-1] + d[i])
    # print(d, cumd)
    ansmin = max(0, 2*max(d)-ansmax)
    # for i in range(N):
    #     res = max(0, 2 * d[i] - ansmax)
    #     print(i, res)
    #     ansmin = min(ansmin, res)
    print(ansmax)
    print(ansmin)


if __name__ == "__main__":
    main()
