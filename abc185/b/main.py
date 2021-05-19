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
    N, M, T = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    now = N
    time = 0
    for i in range(M):
        now -= AB[i][0] - time
        # print(now)
        if now <= 0:
            print('No')
            exit()
        now += AB[i][1] - AB[i][0]
        now = min(now, N)
        time = AB[i][1]
    now -= T - time
    # print(now)
    if now <= 0:
        print('No')
    else:
        print('Yes')


if __name__ == "__main__":
    main()
