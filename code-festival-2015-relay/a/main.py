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
    ans = [0] * 20
    for i in range(10):
        if i % 2 == 0:
            for j in range(1, 21):
                ans[j-1] += 20 * i + j
        else:
            for j in range(1, 21):
                ans[j-1] += 20 * i + (21 - j)
    T = int(input())
    print(ans[T-1])


if __name__ == "__main__":
    main()
