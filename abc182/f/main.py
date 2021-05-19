#!/usr/bin/env python3
import sys
from collections import deque, Counter, defaultdict
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    xs = [0] * N

    # Xを分解する（最小枚数なので一意に定まる）
    for i in range(N):
        xs[N-1-i] = X // A[N-1-i]
        X %= A[N-1-i]

    # print(xs, A)

    # dp[j]: 繰り上がりがj(j=0,1)ある時の場合の数
    dp = [1, 0]
    for i in range(N-1):  # 下の桁から考える
        nextdp = [0, 0]
        if i < N-1:
            nextdp[0] += dp[0]  # 前：繰り上がりなし、次：繰り上がりなし
            if xs[i] < A[i+1]//A[i]-1:  # 前：繰り上がりあり、次：繰り上がりなし
                nextdp[0] += dp[1]

            nextdp[1] += dp[1]  # 前：繰り上がりあり、次：繰り上がりあり
            if xs[i] > 0:
                nextdp[1] += dp[0]
        else:
            pass

        dp = nextdp[:]
        # print(dp)

    print(dp[0]+dp[1])


if __name__ == "__main__":
    main()
