#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7

# Binary indexed tree


class BIT():
    def __init__(self, n):
        self.array = [0] * n
        self.N = n

    # 1番目からi番目までの累積和を求める
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.array[i-1]
            i -= i & (-i)
        return s

    # sum(i,j)
    def sum2(self, i, j):
        return self.sum(j) - self.sum(i-1)

    # i番目にxを追加
    def add(self, i, x):
        while i <= self.N:
            self.array[i-1] += x
            i += i & (-i)


def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [a[-1]] + a[:-1]
    # print(b)
    bit = BIT(N)
    ans = 0
    for i in range(N):
        ans += bit.sum2(b[i] + 1, N)
        bit.add(b[i]+1, 1)
    print(ans, b)

    for j in range(N - 1, 0, -1):
        # tmp = [b[-1]] + b[:-1]
        # b = tmp[:]
        # ans = ans[0] + ans[:-1]
        ans -= bit.sum2(b[j] + 1, N)
        print(ans, b[j]+1)
        bit.add(b[j]+1, -1)
        ans += bit.sum(b[j] + 1)
        bit.add(b[j]+1, 1)
        print(j, ans)


if __name__ == "__main__":
    main()
