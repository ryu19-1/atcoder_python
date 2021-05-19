#!/usr/bin/env python3
from collections import Counter


def main():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))
    p = 998244353
    dp = [[0] * (S+1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(S+1):
            # A[i]を選ばない場合
            dp[i+1][j] += dp[i][j]*2 % p
            # A[i]を選ぶ場合
            if j + A[i] <= S:
                dp[i + 1][j + A[i]] += dp[i][j]

    # print(dp)
    print(dp[N][S] % p)


if __name__ == "__main__":
    main()
