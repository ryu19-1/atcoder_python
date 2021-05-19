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
    N, C = map(int, input().split())
    costs = defaultdict(int)
    for i in range(N):
        a, b, c = map(int, input().split())
        costs[a] += c
        costs[b + 1] -= c
    # print(costs)
    ans = 0
    now = 0  # 現在
    price = 0  # お金
    l = list(dict(costs).items())
    l.sort()
    # print(l)
    #
    for k, v in l:
        # k日までが
        # price += v
        # print(now, k)
        if price < C:
            ans += (k - now) * price
        else:
            ans += (k - now) * C
        price += v
        now = k
    print(ans)


if __name__ == "__main__":
    main()
