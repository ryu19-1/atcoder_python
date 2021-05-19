#!/usr/bin/env python3
import sys
from collections import deque, Counter, defaultdict
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def prime_factorize(N):
    prime_list = []
    while N % 2 == 0:
        prime_list.append(2)
        N //= 2
    f = 3
    while f**2 <= N:
        if N % f == 0:
            prime_list.append(f)
            N //= f
        else:
            f += 2
    if N != 1:
        prime_list.append(N)
    return prime_list


def main():
    A, B = map(int, input().split())
    # A!の中で一度しか出てこない数の個数をカウント
    cnt = defaultdict(int)
    now = B + 1
    while now <= A:
        for p in prime_factorize(now):
            cnt[p] += 1
        now += 1
    # print(cnt)
    cnt = dict(cnt)
    ans = 1
    for k, v in cnt.items():
        # print(k, v)
        ans *= v + 1
        ans %= m
    print(ans)


if __name__ == "__main__":
    main()
