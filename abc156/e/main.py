#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12


def main():
    n, k = map(int, input().split())
    p = 10 ** 9 + 7
    a = [None] * (n+1)
    inva = [None] * (n+1)
    a[0] = 1

    for i in range(1, n+1):
        a[i] = i * a[i-1] % p

    inva[n] = pow(a[n], p-2, p)
    for i in range(n):
        inva[n-i-1] = inva[n-i] * (n-i) % p

    ans = 1
    k = min(k, n-1)
    for i in range(1, k+1):
        res = (a[n] * inva[i] % p) * inva[n - i] % p
        res2 = (a[n - 1] * inva[i] % p) * inva[n - 1 - i] % p
        ans += res * res2 % p
        ans %= p
    print(ans)


if __name__ == "__main__":
    main()
