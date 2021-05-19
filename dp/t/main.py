#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate


def main():
    N = int(input())
    s = input()
    p = 10**9+7

    # dp[i][j]:= i番目まで決めた時、i番目の数より大きい数がj個残っている場合のかず
    dp = [[0] * N for _ in range(N + 1)]
    for j in range(N):
        dp[1][j] = 1

    for i in range(2, N + 1):
        cum = [0] + list(accumulate(dp[i-1]))

        if s[i - 2] == '<':
            for j in range(N - i + 1):
                dp[i][j] += cum[N-i+2]-cum[j+1]
                # for k in range(j + 1, N - i + 2):
                #     dp[i][j] += dp[i - 1][k]
                dp[i][j] %= p
        else:
            for j in range(N - i + 1):
                dp[i][j] += cum[j+1] - cum[0]
                # for k in range(j+1):
                #     dp[i][j] += dp[i - 1][k]
                dp[i][j] %= p
    print(dp[N][0])


if __name__ == "__main__":
    main()
