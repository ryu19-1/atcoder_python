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
    N, X, T = map(int, input().split())
    print((N+(X-1))//X*T)

if __name__ == "__main__":
    main()