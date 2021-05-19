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
    c = input()
    ans = N
    idx = ['A', 'B', 'X', 'Y']
    a = []
    for i in idx:
        for j in idx:
            a.append(i+j)
    for l in range(16):
        for r in range(l+1, 16):
            dp = [0] * (N+1)
            for i in range(N):
                dp[i+1] = dp[i] + 1
                if i > 0 and c[i - 1:i + 1] in (a[l], a[r]):
                    dp[i+1] = min(dp[i+1], dp[i-1]+1)
            ans = min(ans, dp[N])
    print(ans)


if __name__ == "__main__":
    main()
