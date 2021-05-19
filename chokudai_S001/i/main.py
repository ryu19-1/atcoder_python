#!/usr/bin/env python3
import sys
from collections import deque, Counter, defaultdict
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    N = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    ans = 0
    now = 0
    d[now] += 1
    for i in range(N):
        now += a[i]
        ans += d[now - N]
        d[now] += 1
    print(ans)


if __name__ == "__main__":
    main()
