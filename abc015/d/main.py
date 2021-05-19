#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right


def main():
    W = int(input())
    N, K = map(int, input().split())
    dp = [[0] * (W + 1) for _ in range(K+1)]
    for i in range(N):
        A, B = map(int, input().split())
        # print(A, B)
        for j in range(W, -1, -1):
            for k in range(K+1):
                if j + A <= W and k < K:
                    dp[k+1][j + A] = max(dp[k+1][j + A], dp[k][j] + B)
    print(dp[K][W])


if __name__ == "__main__":
    main()
