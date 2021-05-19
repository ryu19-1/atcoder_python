#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right


def main():
    K = input()
    N = len(K)
    D = int(input())
    p = 10 ** 9 + 7
    # dp[k][j][i]:= i桁目までみた時の各桁の総和がj(mod D)の個数
    # k=0:= K未満が確定している
    # k=1:= k未満が確定していない
    dp = [[[0] * (N + 1) for _ in range(D)] for _ in range(2)]
    dp[1][0][0] = 1
    for i in range(1, N + 1):
        d = int(K[i - 1])
        for j in range(D):
            # k=0
            for k in range(10):
                dp[0][(j + k) % D][i] += dp[0][j][i - 1]
            # k=1
            dp[1][(j + d) % D][i] += dp[1][j][i - 1]
            for k in range(d):
                dp[0][(j + k) % D][i] += dp[1][j][i - 1]
        for j in range(D):
            dp[0][j][i] %= p
            dp[1][j][i] %= p
    print((dp[0][0][N]+dp[1][0][N]-1) % p)


if __name__ == "__main__":
    main()
