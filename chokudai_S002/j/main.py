#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate
from math import gcd

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    N = int(input())
    # ans = 0
    dp = [0, 0]
    for _ in range(N):
        A, B = map(int, input().split())
        dp = [max(gcd(dp[0], A), gcd(dp[1], A)),
              max(gcd(dp[0], B), gcd(dp[1], B))]
    print(max(dp))


if __name__ == "__main__":
    main()
