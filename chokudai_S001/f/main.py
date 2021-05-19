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
    now = a[0]
    ans = 1
    for i in range(1, N):
        if now < a[i]:
            ans += 1
        now = max(now, a[i])
    print(ans)


if __name__ == "__main__":
    main()
