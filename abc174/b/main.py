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
    N, D = map(int, input().split())
    ans = 0
    for i in range(N):
        x, y = map(int, input().split())
        if x**2 + y**2 <= D**2:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
