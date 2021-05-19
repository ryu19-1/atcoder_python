#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def f(n):
    res = 0
    for r in [*str(n)]:
        res += int(r)
    # print(n, list(str(n)))
    # print(n, res)
    return res


def main():
    N = int(input())
    ans = set()
    L = len(str(N))
    # print(N, L)
    for i in range(1, L + 1):
        for j in range(1, 9 * i + 1):
            if N - j < 0:
                break
            if f(N - j) + N - j == N:
                ans.add(N - j)
    print(len(ans))
    for a in sorted(ans):
        print(a)


if __name__ == "__main__":
    main()
