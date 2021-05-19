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
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if (xy[j][1] - xy[i][1]) * (xy[k][0] - xy[j][0]) == (xy[j][0] - xy[i][0]) * (xy[k][1] - xy[j][1]):
                    print('Yes')
                    exit()
    print('No')


if __name__ == "__main__":
    main()
