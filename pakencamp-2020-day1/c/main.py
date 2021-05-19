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
    ans = [set() for _ in range(N)]
    for i in range(N):
        k = int(input())
        S = list(input().split())
        for s in S:
            ans[i].add(s)
    # print(ans)
    res = ans[0]
    for i in range(1, N):
        res = res & ans[i]
    print(len(res))


if __name__ == "__main__":
    main()
