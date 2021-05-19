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
    a = list(map(int, input().split()))
    ans = 0
    digit = 0
    for i in range(N-1, -1, -1):
        ans += a[i] * pow(10, digit, m) % m
        digit += len(str(a[i]))
    print(ans % m)


if __name__ == "__main__":
    main()
