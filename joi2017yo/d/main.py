#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

INF = 10**12

def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(N)]

    accum = [None for _ in range(M)]
    for i in range(M):
        tmp = [0] * (N+1)
        for j in range(N):
            tmp[j+1] += int(A[j]==i+1)
            if j < N-1:
                tmp[j+2] += tmp[j+1]
        accum[i] = tmp

    # bit DP
    dp = [-1] * (2**M)
    dp[0] = 0
    nums = [0] * (2**M)
    for j in range(2**M):
        for k in range(M):
            if j >> k & 1:
                nums[j] += accum[k][-1]

    for i in range(M):# M種類
        for j in range(2**M):
            if dp[0] < 0: continue
            l = nums[j] # 今のところどれだけぬいぐるみが配置されているか
            for k in range(M):
                if j >> k & 1: continue
                r = l + accum[k][-1]
                dp[j | 1 << k] = max(dp[j | 1 << k], dp[j] + accum[k][r] - accum[k][l])
    print(N-dp[-1])

if __name__ == "__main__":
    main()
