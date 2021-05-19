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
    ans = set()
    for _ in range(N):
        A, B = map(int, input().split())
        if A > B:
            A, B = B, A
        ans.add(A * INF + B)
    print(len(ans))


if __name__ == "__main__":
    main()
