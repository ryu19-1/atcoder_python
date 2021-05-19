#!/usr/bin/env python3
import sys


sys.setrecursionlimit(10**6)


X, Y, A, B = map(int, input().split())
ans = 0


def DFS(now, exp):
    global ans
    if now < Y:
        ans = max(ans, exp+(Y-now-1)//B)
        DFS(now*A, exp+1)
        # DFS(now+B, exp+1)


DFS(X, 0)
print(ans)
