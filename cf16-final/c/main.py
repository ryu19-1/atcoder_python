#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


class UnionFind():
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.size[x] < self.size[y]:
                x, y = y, x
            self.parents[y] = x
            self.size[x] += self.size[y]


def main():
    N, M = map(int, input().split())
    uf = UnionFind(N + M)
    for i in range(N):
        L = list(map(int, input().split()))
        for l in L[1:]:
            uf.union(i + M, l - 1)

    ans = set()
    for i in range(M, M + N):
        ans.add(uf.find(i))
    if len(ans) == 1:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()
