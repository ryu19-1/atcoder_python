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
    dx = [0, 1, 0, 1]
    dy = [0, 0, 1, 1]

    ans = 0
    for i in range(H - 1):
        for j in range(W - 1):
            cnt = 0
            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]
                if S[y][x] == '#':
                    cnt += 1
            if cnt == 1 or cnt == 3:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
