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
    A = [None] * N
    B = [None] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    l = []
    now = sum(A)
    for i in range(N):
        l.append([A[i]*2+B[i], A[i]])
    l.sort()
    ans = 0
    piyo = 0
    while now >= piyo:
        x, y = l.pop()
        piyo += x-y
        now -= y
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
