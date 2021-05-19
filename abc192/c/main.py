#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def cal(a):
    L = len(str(a))
    g1 = sorted(list(str(a)), reverse=True)
    g1 = int(''.join(g1))
    g2 = sorted(list(str(a)))
    g2 = int(''.join(g2))
    return g1 - g2


def main():
    N, K = map(int, input().split())
    a = [N]
    for i in range(K):
        a.append(cal(a[-1]))
    print(a[-1])


if __name__ == "__main__":
    main()
