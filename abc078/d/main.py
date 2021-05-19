#!/usr/bin/env python3
import sys

sys.setrecursionlimit(10**6)
INF = 10**12
N, Z, W = map(int, input().split())
a = [Z] + list(map(int, input().split()))

def rec(X,Y,i,count):# i枚目まで取った
    if i == N:# 山札がないので得点計算して更新
        return abs(X-Y)
    else:
        if count % 2 == 0:# 今はXのターン
            tmp = -INF
            for j in range(i+1,N+1):
                tmp = max(tmp, rec(a[j], Y, j, count+1))
            return tmp
        else:# 今はYのターン
            tmp = INF
            for j in range(i+1,N+1):
                tmp = min(tmp, rec(X, a[j], j, count+1))
            return tmp

ans = rec(Z,W,0,0)
print(ans)