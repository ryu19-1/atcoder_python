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
    a, b = map(int, input().split())
    N = int(input())
    x = set()
    for i in range(N):
        x.add(tuple(map(lambda x: int(x)-1, input().split())))

    dp = [[0]*a for _ in range(b)]
    dp[0][0] = 1
    for i in range(b):
        for j in range(a):
            if i==j==0: continue
            if (j,i) in x: continue
            if j > 0: dp[i][j] += dp[i][j-1]
            if i > 0: dp[i][j] += dp[i-1][j]
    print(dp[b-1][a-1])

if __name__ == "__main__":
    main()
