#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    memo = [1] * (N + 1)
    for i in range(1, N+1):
        memo[i] = memo[i-1] * i % m
    # print(memo)
    for i in range(N):
        res = (a[i] - 1) * memo[N - 1 - i] % m
        ans += res
        print(i, ans)
    print(ans % m)


if __name__ == "__main__":
    main()
