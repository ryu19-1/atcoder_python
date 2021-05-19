#!/usr/bin/env python3
import sys
from collections import Counter

sys.setrecursionlimit(10**6)


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
    M = 400000
    adj = [[] for _ in range(M)]
    for _ in range(N):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        # adj[b-1].append(a-1)

    uf = UnionFind(M)
    loop = [False] * M
    for i in range(M):
        for j in adj[i]:
            # iとjがループだったら
            if uf.find(i) == uf.find(j):
                loop[uf.find(i)] = True
            else:
                uf.union(i, j)
    l = Counter([uf.find(i) for i in range(M)])
    # print(l)
    ans = 0
    for k, v in l.items():
        # print(k, v)
        if loop[k]:
            ans += v
        else:
            ans += v - 1
    print(ans)


if __name__ == "__main__":
    main()
