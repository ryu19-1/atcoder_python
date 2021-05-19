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
    S1 = input()
    N = len(S1)//2
    S1 = Counter(S1)
    S2 = Counter(input())
    S3 = Counter(input())
    mins1 = 0
    maxs1 = 0
    for i in range(26):
        mins1 += max(0, S3[chr(65+i)]-S2[chr(65+i)])
        maxs1 += min(S1[chr(65 + i)], S3[chr(65 + i)])
    # print(mins1, maxs1)
    if mins1 <= N <= maxs1:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()
