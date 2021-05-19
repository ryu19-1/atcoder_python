#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right


def main():
    N = int(input())
    A = list(map(int, input().split()))
    dp = A[:]
    # print(dp)
    for k in range(1, N):  # 区間の長さ
        if k % 2 == 0:  # 最大化したい
            nextdp = [None] * (N - k)
            for i in range(N - k):
                nextdp[i] = max(dp[i] + A[i + k], dp[i + 1] + A[i])
        else:
            nextdp = [None] * (N - k)
            for i in range(N - k):
                nextdp[i] = min(dp[i] - A[i + k], dp[i + 1] - A[i])
        dp = nextdp[:]
    if N % 2 == 0:
        print(-dp[0])
    else:
        print(dp[0])


if __name__ == "__main__":
    main()
