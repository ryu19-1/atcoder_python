#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    m = 10**9 + 7

    dp = [0] * W
    for i in range(H):
        for j in range(W):
            if i == j == 0:
                dp[j] = 1
                continue
            if a[i][j] == '.':
                if j > 0:
                    dp[j] = (dp[j] + dp[j-1]) % m
            else:
                dp[j] = 0
    print(dp[W-1])

if __name__ == "__main__":
    main()
