#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right


def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    p = 10**9+7
    dp = [0] * (K + 1)
    dp[0] = 1
    for i in range(N):
        accum = 0
        nextdb = [0] * (K+1)
        for j in range(K + 1):
            accum += dp[j]
            if j > a[i]:
                accum -= dp[j - a[i]-1]
            nextdb[j] = accum % p
        dp = nextdb[:]
    print(dp[K])


if __name__ == "__main__":
    main()
