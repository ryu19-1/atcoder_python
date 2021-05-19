#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate
from math import pi

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    N, Q = map(int, input().split())
    XRH = [list(map(int, input().split())) for _ in range(N)]
    V = [None] * N
    for i in range(N):
        V[i] = XRH[i][1] ** 2 * pi * XRH[i][2] / 3
    # print(V)
    for _ in range(Q):
        ans = 0
        A, B = map(int, input().split())
        # print(A, B)
        for i in range(N):
            x, r, h = XRH[i]
            if x + h <= A:
                continue
            elif x <= A:
                if x + h <= B:
                    ans += V[i]*((x+h-A)**3/(h**3))
                elif x <= B:
                    ans += V[i]*(((x+h-A)**3/(h**3)) - ((x+h-B)**3/(h**3)))
            else:
                if x + h <= B:
                    ans += V[i]
                elif x <= B:
                    ans += V[i] * (1 - ((x+h-B)**3/(h**3)))
        print(ans)


if __name__ == "__main__":
    main()
