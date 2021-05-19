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
    # N番目はy=-100, N+1番目はy=100
    q = []
    for i in range(N):
        for j in range(i + 1, N):
            dis = (xy[j][0] - xy[i][0]) ** 2 + (xy[j][1] - xy[i][1]) ** 2
            heappush(q, (dis**0.5, i, j))
    for i in range(N):
        heappush(q, (xy[i][1]+100, i, N))
        heappush(q, (100 - xy[i][1], i, N + 1))
    # print(q)
    uf = UnionFind(N + 2)
    while len(q) > 0:
        d, i, j = heappop(q)
        # print(d, i, j)
        uf.union(i, j)
        if uf.find(N) == uf.find(N + 1):
            print(d/2)
            exit()


if __name__ == "__main__":
    main()
