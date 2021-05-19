#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_left
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    N = int(input())
    a = list(map(int, input().split()))
    dp = [INF] * N
    for i in range(N):
        d = bisect_left(dp, a[i])
        dp[d] = a[i]
        # print(i, dp)
    ans = bisect_left(dp, INF)
    print(ans)


if __name__ == "__main__":
    main()
