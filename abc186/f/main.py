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
    H, W, M = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(M)]
    # XY.sort()
    c = [H] * W  # 各列で飛車の駒が移動できるマスの数
    for i in range(M):
        c[XY[i][1] - 1] = min(c[XY[i][1] - 1], XY[i][0]-1)
    # XYを各行ごとに持ち直す
    xy = [[] for _ in range(H)]
    for i in range(M):
        xy[XY[i][0] - 1].append(XY[i][1] - 1)

    b = BIT(W)
    checked = [0] * W
    if len(xy[0]) == 0:
        ans = sum(c)
    else:
        ans = sum(c[:min(xy[0])])
        for k in range(min(xy[0]), W):
            b.add(k+1, 1)
            checked[k] = 1

    for i in range(H):
        xy[i].sort()
        if len(xy[i]) == 0:
            p = W
        else:
            p = xy[i][0]
        if p == 0:
            break
        ans += b.sum(p)
        for j in xy[i]:
            if checked[j] == 0:
                b.add(j+1, 1)
                checked[j] = 1
    print(ans)


if __name__ == "__main__":
    main()
