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
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if sum(A) != sum(B):
        print('No')
        exit()

    uf = UnionFind(N)
    for _ in range(M):
        c, d = map(lambda x: int(x) - 1, input().split())
        uf.union(c, d)

    sumdict = [[] for _ in range(N)]
    for i in range(N):
        sumdict[uf.parents[uf.find(i)]].append(i)

    for i in range(N):
        asum = 0
        bsum = 0
        # print(sumdict[i])
        for s in sumdict[i]:
            asum += A[s]
            bsum += B[s]
        if asum != bsum:
            print('No')
            exit()
    print('Yes')


if __name__ == "__main__":
    main()
