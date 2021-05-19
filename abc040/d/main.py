#!/usr/bin/env python3
from heapq import heappop, heappush
import sys
input = sys.stdin.readline


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
    q = []
    for _ in range(M):
        a, b, y = map(int, input().split())
        heappush(q, (-y, a - 1, b - 1))

    uf = UnionFind(N)
    q2 = []
    Q = int(input())
    for i in range(Q):
        v, w = map(int, input().split())
        heappush(q2, (-w, v - 1, i))

    ans = [None] * Q
    while len(q2) > 0:
        w, v, i = heappop(q2)
        # wよりも新しい物は全て取り出す
        while len(q) > 0:
            y, a, b = heappop(q)
            if w > y:
                uf.union(a, b)
            else:
                heappush(q, (y, a, b))
                break
        ans[i] = uf.size[uf.find(v)]
    [print(a) for a in ans]


if __name__ == "__main__":
    main()
