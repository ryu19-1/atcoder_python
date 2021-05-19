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
    a = list(map(int, input().split()))
    # accuma = [0] + [*accumulate(a)]
    # for i in range(1, N+1):
    #     for j in range(i + 1, N + 1):
    #         if accuma[j]-accuma[i-1] == 476:
    #             print(i, j, accuma[j]-accuma[i-1])
    # print(accuma)
    suma = sum(a)
    # print(suma)
    r = 0
    sumnow = 0
    ans = INF
    for l in range(N):
        # print(l, r)
        while r < N and 2 * (sumnow + a[r]) < suma:
            sumnow += a[r]
            ans = min(ans, abs(2 * sumnow - suma))
            # print(l, r, sumnow, abs(2 * sumnow - suma))
            r += 1
        # print(l, r, sumnow, abs(2 * sumnow - suma))
        if r < N:
            ans = min(ans, abs(2 * (sumnow+a[r]) - suma))
        if (l == r):
            r += 1
        else:
            sumnow -= a[l]
    print(ans)


if __name__ == "__main__":
    main()
