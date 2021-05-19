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
    p = list(map(int, input().split()))
    ans = [*range(200000)]
    ans2 = set(ans)
    for i in range(N):
        if p[i] in ans2:
            ans.remove(p[i])
            ans2.remove(p[i])
        print(ans[0])


if __name__ == "__main__":
    main()
