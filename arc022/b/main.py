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
    A = list(map(lambda x: int(x)-1, input().split()))
    ans = 1
    l = 0
    r = 0
    tastes = [0]*(10**5)

    while r < N:
        if tastes[A[r]] == 0:
            ans = max(ans, r-l+1)
            tastes[A[r]] = 1
            r += 1
        else:
            tastes[A[l]] = 0
            l += 1
            if l > r:
                r += 1
    print(ans)


if __name__ == "__main__":
    main()
