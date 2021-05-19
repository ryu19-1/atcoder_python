#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    H, N = map(int, input().split())
    A = [None] * N
    B = [None] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    # INF = 10**12
    # dp = [[INF]*(H+1) for _ in range(N+1)]
    # dp[0][0] = 0
    # for i in range(N):
    #     for j in range(H+1):
    #         dp[i+1][j] = min(dp[i+1][j], dp[i][j])
    #         dp[i+1][min(j+A[i],H)] = min(dp[i+1][min(j+A[i],H)],dp[i+1][j]+B[i])
    # print(dp[N][H])

    #1次元DPに書き換え
    INF = 10**12
    dp = [INF] * (H+1)
    dp[0] = 0
    for i in range(N):
        for j in range(H+1):
            dp[min(j+A[i],H)] = min(dp[min(j+A[i],H)],dp[j]+B[i])
    print(dp[H])

if __name__ == "__main__":
    main()
