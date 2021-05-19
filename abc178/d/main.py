#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12


def main():
    N = int(input())

    p = 10**9+7
    a = [None] * (N+1)
    inva = [None] * (N+1)
    a[0] = 1

    for i in range(1, N+1):
        a[i] = i * a[i-1] % p

    inva[N] = pow(a[N], p-2, p)
    for i in range(N):
        inva[N - i - 1] = inva[N - i] * (N - i) % p

    ans = 0
    S = N
    cnt = 0
    while S >= 3:
        S -= 3
        cnt += 1
        tmp = a[cnt + S - 1] * inva[S] % p
        tmp = tmp * inva[cnt - 1] % p
        ans += tmp
        ans %= p
    print(ans)


if __name__ == "__main__":
    main()
