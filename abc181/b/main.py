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
    ans = 0
    for _ in range(N):
        a, b = map(int, input().split())
        ans += (a + b) * (b - a + 1) // 2
    print(ans)


if __name__ == "__main__":
    main()
