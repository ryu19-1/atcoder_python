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
    a = list(map(int, input().split()))
    accuma = list(accumulate(a))
    ans = 0
    tmpa = [None] * N
    tmpa[0] = accuma[0]
    for i in range(1, N):
        if accuma[i] >= tmpa[i - 1]:
            tmpa[i] = accuma[i]
        else:
            tmpa[i] = tmpa[i - 1]
    # print(tmpa)
    # print(accuma)
    now = 0
    for i in range(N):
        # print(ans, now+accuma[i], now+tmpa[i])
        ans = max(ans, now+accuma[i], now+tmpa[i])
        now += accuma[i]
    print(ans)


if __name__ == "__main__":
    main()
