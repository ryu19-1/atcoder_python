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
    N, K = map(int, input().split())
    cnt = [0] * (2 * N+1)
    # a+bの個数を調べる
    cnt[2] = 1
    for i in range(3, N + 2):
        cnt[i] = cnt[i - 1] + 1

    for i in range(N + 2, 2 * N + 1):
        cnt[i] = cnt[i - 1] - 1

    ans = 0
    for i in range(2 * N + 1):
        if 0 <= i-K <= 2*N:
            ans += cnt[i] * cnt[i-K]
    print(ans)


if __name__ == "__main__":
    main()
