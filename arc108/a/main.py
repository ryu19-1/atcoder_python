#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def cal_divisors(N):
    divisors = []
    i = 1
    while i*i <= N:
        if N % i == 0:
            divisors.append(i)
            if i != N // i:
                divisors.append(N//i)
        i += 1
    divisors.sort()
    return divisors


def main():
    S, P = map(int, input().split())
    divisors = cal_divisors(P)
    for d in divisors:
        if d + P // d == S:
            print('Yes')
            exit()
    print('No')


if __name__ == "__main__":
    main()
