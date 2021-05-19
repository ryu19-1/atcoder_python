#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**24
m = 10**9 + 7


def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [set() for _ in range(N)]
    dp[0] = set(A)
    ans = X-max(A)
    for k in range(2, N + 1):
        tmpX = X % k
        for d in dp[k - 2]:
            dp[k-1].add()
        # q = []
        # for i in range(N):
        #     if A[i] % k == tmpX:
        #         heappush(q, (-A[i]))
        # res = 0
        # for i in range(k):
        #     if len(q) == 0:
        #         break
        #     res -= heappop(q)
        # else:
        #     print(k, res)
        #     ans = min(ans, (X - res) // k)
    print(ans)


if __name__ == "__main__":
    main()
