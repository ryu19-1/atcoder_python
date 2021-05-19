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
    N, M = map(int, input().split())
    if M == 0:
        print(1)
        exit()
    A = list(map(int, input().split()))
    A.sort()
    white = []
    now = 1
    if A[0] - 1 > 0:
        white.append(A[0] - 1)
    now = A[0]
    for i in range(1, M):
        # print(A[i])
        if A[i] - now - 1 > 0:
            white.append(A[i] - now-1)
        now = A[i]
    if N - now > 0:
        white.append(N - now)
    # print(white)
    if len(white) == 0:
        print(0)
        exit()
    W = min(white)
    # print(W, white)
    ans = 0
    for w in white:
        ans += (w + W - 1) // W
    print(ans)


if __name__ == "__main__":
    main()
