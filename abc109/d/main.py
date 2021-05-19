#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7

H, W = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]

def main():
    count = 0
    ans = []
    for i in range(H):
        for j in range(W-1):
            if a[i][j] & 1:
                ans.append([i+1, j+1, i+1, j+2])
                a[i][j+1] += 1
                count += 1

    for i in range(H-1):
        if a[i][W-1] & 1:
            ans.append([i+1, W, i+2, W])
            a[i+1][W-1] += 1
            count += 1

    print(count)
    [print(*a) for a in ans]

if __name__ == "__main__":
    main()
