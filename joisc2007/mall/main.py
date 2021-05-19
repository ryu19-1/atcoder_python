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
    m, n = map(int, input().split())
    a, b = map(int, input().split())
    c = [[None] * (m+1) for _ in range(n+1)]
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(m):
            if tmp[j] == -1:
                c[i + 1][j + 1] = INF
            else:
                c[i+1][j+1] = tmp[j]

    # 累積和
    for i in range(n-1):
        for j in range(m):
            if j < m:
                c[i][j + 1] += c[i][j]
            c[i + 1][j] += c[i][j]

    ans = INF
    for i in range(n - b):
        for j in range(m - a):
            res = c[i+b+1][j+a+1] - c[i][j+a+1] - c[i+b+1][j] + c[i][j]
            ans = min(res, ans)
    print(ans)


if __name__ == "__main__":
    main()
