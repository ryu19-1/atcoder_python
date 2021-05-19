#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate
from math import gcd

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0] * 1001
    for i in range(N):
        for k in range(2, 1001):
            if A[i] % k == 0:
                cnt[k] += 1
    print(cnt.index(max(cnt)))
    # print(cnt)


if __name__ == "__main__":
    main()
