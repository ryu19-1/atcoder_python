#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N, M = map(int, input().split())
    D = [int(input()) for _ in range(N)]
    C = [int(input()) for _ in range(M)]

    INF = 10**12
    dp = [[INF]*(N+1) for _ in range(M+1)]
    dp[0][0] = 0
    
    # 配るDPをかく
    for i in range(M):
        for j in range(N):
            # 移動しない
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            # 移動する
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+C[i]*D[j])
    print(dp[N][M])

if __name__ == "__main__":
    main()
