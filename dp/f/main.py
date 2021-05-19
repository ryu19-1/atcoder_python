#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
import sys
sys.setrecursionlimit(10**6)

s = input()
t = input()
N = len(s)
M = len(t)
ans = []

def print_lcs(dp,i,j):
    global ans
    if i == 0 or j == 0:
        return
    if s[i-1] == t[j-1]:
        print_lcs(dp,i-1,j-1)
        ans.append(s[i-1])
    else:
        if dp[i-1][j] >= dp[i][j-1]:
            print_lcs(dp,i-1,j)
        else:
            print_lcs(dp,i,j-1)


def main():
    dp = [[0]*(M+1) for _ in range(N+1)]
    
    for i in range(N):
        for j in range(M):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    
    print_lcs(dp,N,M)
    print(''.join(ans))

if __name__ == "__main__":
    main()
