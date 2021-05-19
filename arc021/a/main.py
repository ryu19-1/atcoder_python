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
    A = [list(map(int, input().split())) for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if i < 3 and A[i][j] == A[i + 1][j]:
                print('CONTINUE')
                exit()
            if j < 3 and A[i][j] == A[i][j+1]:
                print('CONTINUE')
                exit()
    print('GAMEOVER')


if __name__ == "__main__":
    main()
