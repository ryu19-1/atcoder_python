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
    nico = [2525, 252525, 25252525]
    N = int(input())
    ans = N // 25
    for i in range(3):
        now = nico[i]
        while now <= N:
            if now % 25 != 0:
                ans += 1
            now += nico[i]
    print(ans)


if __name__ == "__main__":
    main()
