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
    N, K = map(int, input().split())
    wp = [list(map(int, input().split())) for _ in range(N)]
    now = [0, 0]
    for i in range(min(N, K)):
        decide = 0
        now2 = (now[0] + wp[0][0] * wp[0][1], now[1] + wp[0][0])
        for j in range(1, len(wp)):
            tmpL = now[1] + wp[j][0]
            tmpS = now[0] + wp[j][0] * wp[j][1]
            if tmpL * now2[0] <= tmpS * now2[1]:
                decide = j
                now2 = [tmpS, tmpL]
        del wp[decide]
        # print(wp)
        # print(now2)
        now = now2[:]
    print(now[0]/now[1])


if __name__ == "__main__":
    main()
