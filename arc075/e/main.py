#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_left
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
    N, K = map(int, input().split())
    a = [int(input()) for _ in range(N)]
    b = [0] * N
    b[0] = a[0]-K
    # print(a)
    for i in range(N - 1):
        b[i + 1] += b[i] + a[i + 1] - K
    b = [0] + b
    # print(b)
    bb = [0] * (N+1)
    c = sorted(set(b))
    for i in range(N + 1):
        bb[i] = bisect_left(c, b[i])
    # print(bb)

    ans = 0
    bit = BIT(N+1)
    # bit.add(bb[0]+1, 1)
    for i in range(N+1):
        # print(bb[i]+1)
        ans += bit.sum(bb[i]+1)
        bit.add(bb[i]+1, 1)
    print(ans)


if __name__ == "__main__":
    main()
