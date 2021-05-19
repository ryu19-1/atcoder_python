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
    l = [25, 39, 51, 76, 163, 111, 136, 128, 133, 138]
    K = len(l)
    ans = set()
    for i in range(2 ** K):
        for j in range(K):
            res = 0
            if i >> j & 1:
                res += l[j]
        ans.add(res)
        if i >> 6 & 1:
            ans.add(res-136+58)
    for a in sorted(ans):
        print(a)


if __name__ == "__main__":
    main()
