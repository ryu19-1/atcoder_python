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
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    l = 0
    r = N - 1
    while r > l:
        ans += (A[r] - A[l]) * (r-l)
        l += 1
        r -= 1
    print(ans)


if __name__ == "__main__":
    main()
