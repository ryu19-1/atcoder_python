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
    ans = [0] * N
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        ans[a] = 1-ans[a]
        ans[b] = 1-ans[b]
    if 1 in ans:
        print('NO')
    else:
        print('YES')

if __name__ == "__main__":
    main()
