#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    abc = [None] * N

    for i in range(N):
        abc[i] = list(map(int, input().split()))
    
    dp = [[0]*3 for _ in range(N+1)]# a,b,c

    for i in range(N):
        for j in range(3):
            dp[i+1][j] = max(dp[i][(j+1)%3]+abc[i][(j+1)%3], dp[i][(j+2)%3]+abc[i][(j+2)%3])
    print(max(dp[N]))

if __name__ == "__main__":
    main()
