#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    S = input()
    N = len(S)
    p = 10**9 + 7
    dp = [[0]*13 for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(N):
        if S[i] == '?':
            for j in range(13):
                for k in range(10):
                    dp[i+1][(10*j+k)%13] += dp[i][j]
                    dp[i+1][(10*j+k)%13] %= p
        else:
            s = int(S[i])
            for j in range(13):
                dp[i+1][(10*j+s)%13] = dp[i][j]
    print(dp[N][5])
    

if __name__ == "__main__":
    main()
