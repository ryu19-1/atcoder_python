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
    N, W = map(int, input().split())
    w = [None] * N
    v = [None] * N
    for i in range(N):
        w[i], v[i] = map(int, input().split())

    # dp[j]:  
    dp = [0] * (W+1)

    for i in range(N):
        for j in range(W):
            if j-w[j] >= 0:
                dp[j] = max(dp[j], dp[j-w[j]]+v[j])
    print(dp)

if __name__ == "__main__":
    main()
