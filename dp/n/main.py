#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right


def main():
    N = int(input())
    a = list(map(int, input().split()))
    INF = 10 ** 18
    # dp[i][j]: i~jまでの区間のスライムを1匹にするまでのコストの最小値
    dp = [[INF] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0

    for k in range(1, N):


if __name__ == "__main__":
    main()
