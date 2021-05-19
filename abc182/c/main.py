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
    N = input()
    k = len(N)
    ans = INF
    for i in range(1, 2 ** k):
        res = 0
        cnt = 0
        for j in range(k):
            if i >> j & 1:
                res += int(N[j])
                cnt += 1
        if res % 3 == 0:
            ans = min(ans, k - cnt)
    if ans == INF:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
