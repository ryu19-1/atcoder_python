#!/usr/bin/env python3
from collections import deque, Counter, defaultdict
import sys
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
        return x  # 親の方を返す


N, Q = map(int, input().split())
C = list(map(lambda x: int(x) - 1, input().split()))
# clist[i][j]: i番目の人のグループ内でクラスjに所属する人数
clist = [defaultdict(int) for _ in range(N)]
for i in range(N):
    clist[i][C[i]] = 1

uf = UnionFind(N)

for _ in range(Q):
    query = list(map(lambda x: int(x) - 1, input().split()))
    # print(query)
    if query[0] == 0:
        x = uf.find(query[1])
        y = uf.find(query[2])
        if x != y:
            # query[1]がquery[2]の親になる
            r = uf.union(x, y)
            if r != x:  # yが親になっている
                x, y = y, x
            # sizeが小さい方をsizeが大きい方に足している
            # ある要素がマージされるごとに所属する集合の大きさは2倍以上になる-> 最大でもlogN回しかマージされない
            # 全体でもO(NlogN)
            for k, v in clist[y].items():
                clist[x][k] += v
    else:
        print(clist[uf.find(query[1])][query[2]])
