#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


# def convert10to8(N):


def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if '7' not in str(i) and '7' not in str(oct(i)):
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
