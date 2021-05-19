#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    h = list(map(int, input().split()))
    INF = 10**12
    dp = [INF] * (N+1)
    dp[1] = 0
    for i in range(1,N):
        dp[i+1] = min(dp[i+1],dp[i]+abs(h[i-1]-h[i]))
        if i < N-1:
            dp[i+2] = min(dp[i+2],dp[i]+abs(h[i-1]-h[i+1]))
    print(dp[N])

if __name__ == "__main__":
    main()
