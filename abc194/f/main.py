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
    N, K = input().split()
    K = int(K)
    L = len(N)
    ans = 0
    digit = list('0123456789ABCDEF')
    used = set()
    for i in range(L):
        # 上からi桁目で初めて小さいことが確定する時
        used.add(N[i])
        if len(used) > K:
            break

    print(ans)


if __name__ == "__main__":
    main()
