#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
p = 998244353

N, K = map(int, input().split())
A = list(map(int, input().split()))

now = 2 * sum(A) % m
print(now)

for _ in range(2, K + 1):
    sumA = sum(A) % p
    aN = 0
    for j in range(N):
        aN += pow(A[j], i, p)
        aN %= p
    res = pow(sumA, i, p) - aN
    res %= p
    res * inva[]


if __name__ == "__main__":
    main()
