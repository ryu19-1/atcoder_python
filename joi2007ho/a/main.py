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
    N, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    now = sum(A[:K])
    ans = now
    for i in range(1,N-K+1):
        now += A[i+K-1] - A[i]
        ans = max(ans, now)
    print(ans)

if __name__ == "__main__":
    main()
