#!/usr/bin/env python3
import sys
from collections import deque, Counter
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
    N = int(input())
    ans = 0
    for p in Counter(prime_factorize(N)).items():
        cnt = 0
        now = p[0]
        while cnt <= p[1]:
            tmp = now
            while tmp % p[0] == 0:
                tmp //= p[0]
                cnt += 1
            now += p[0]
        ans = max(ans, now)
    print(ans)


if __name__ == "__main__":
    main()
