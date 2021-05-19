#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(H):
        for j in range(W):
            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]
                if 0 <= y < H and 0 <= x < W:
                    if S[i][j] == S[y][x] == '.':
                        ans += 1
    print(ans//2)


if __name__ == "__main__":
    main()
