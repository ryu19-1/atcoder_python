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
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    ans = [None] * N
    for i in range(N):
        ans[i] = xy[i][0]-1
    xy.sort()
    # print(xy)
    miny = [None] * N
    miny[0] = xy[0][1]
    for i in range(1, N):
        miny[i] = min(miny[i - 1], xy[i][1])
    # print(miny)

    maxy = [None] * N
    maxy[N - 1] = xy[N - 1][1]
    for i in range(N - 2, -1, -1):
        maxy[i] = max(maxy[i + 1], xy[i][1])
    # print(maxy)

    uf = UnionFind(N)
    for i in range(N - 1):
        # iとi+1が連結か考える
        if miny[i] != N - i:
            uf.union(i, i + 1)
            # print(i, i+1)
    # print(uf.parents)
    for i in range(N):
        print(uf.size[uf.find(ans[i])])


if __name__ == "__main__":
    main()
