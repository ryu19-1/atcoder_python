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
    A = list(map(int, input().split()))
    check = [[] for _ in range(N)]
    for i in range(N):
        check[A[i]].append(i)
    # print(check)

    for i in range(N):
        tmp = [-1] + check[i] + [N]
        L = len(tmp)
        # print(i, tmp)
        flg = False
        for j in range(L - 1):
            diff = tmp[j + 1] - tmp[j]
            if diff > M:
                flg = True
                break
        if flg:
            print(i)
            exit()
    else:
        print(N)


if __name__ == "__main__":
    main()
