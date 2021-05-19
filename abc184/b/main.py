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
    N, X = map(int, input().split())
    S = input()
    ans = X
    for i in range(N):
        if S[i] == 'o':
            ans += 1
        else:
            ans = max(0, ans - 1)
    print(ans)


if __name__ == "__main__":
    main()
