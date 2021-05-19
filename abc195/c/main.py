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
    N = input()
    L = len(N)
    ans = 0
    for i in range(L):
        if i > 0 and i % 3 == 0:
            # print(i, N[L - 1 - i])
            ans += int(N) - pow(10, i) + 1
    print(ans)


if __name__ == "__main__":
    main()
