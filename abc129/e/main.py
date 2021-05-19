#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right


def main():
    L = input()
    N = len(L)
    m = 10**9+7
    dp = [[0] * 2 for _ in range(N + 1)]  # 0: L以下が確定している/1: L以下が確定していない
    dp[0][1] = 1
    for i in range(N):
        # 既にa+b<=Lが確定しているなら何を入れてもいい
        dp[i + 1][0] += 3 * dp[i][0]
        if L[i] == '0':
            # a+b=Lの状況だと(0,0)しか遷移しない
            dp[i + 1][1] += dp[i][1]
        else:
            # a+b=Lだと(1,0),(0,1)が遷移
            dp[i + 1][1] += 2 * dp[i][1]
            dp[i + 1][0] += dp[i][1]
        dp[i+1][0] %= m
        dp[i + 1][1] %= m

    print(sum(dp[N]) % m)


if __name__ == "__main__":
    main()
