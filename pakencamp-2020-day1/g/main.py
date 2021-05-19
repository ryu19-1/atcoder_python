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
    lrx = [list(map(int, input().split())) for _ in range(M)]
    ans = -1
    for i in range(1 << N):
        check = [0] * N
        for j in range(N):
            if (1 << j) & i:
                check[j] = 1
        for k in range(M):
            if sum(check[lrx[k][0] - 1:lrx[k][1]]) != lrx[k][2]:
                break
        else:
            ans = max(ans, sum(check))
    print(ans)


if __name__ == "__main__":
    main()
