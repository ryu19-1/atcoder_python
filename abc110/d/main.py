#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12


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
    N, M = map(int, input().split())
    prime_list = prime_factorize(M)
    # p = Counter(prime_list)
    ans = 1

    N += 100
    p = 10**9+7
    a = [None] * (N+1)
    inva = [None] * (N+1)
    a[0] = 1

    for i in range(1, N+1):
        a[i] = i * a[i-1] % p

    inva[N] = pow(a[N], p-2, p)
    for i in range(N):
        inva[N - i - 1] = inva[N - i] * (N - i) % p

    N -= 100
    for prime in Counter(prime_list).items():
        # print(prime)
        # nHr = n+r-1Hr
        tmp = (a[N + prime[1] - 1] * inva[N - 1] % p) * inva[prime[1]] % p
        ans *= tmp
        ans %= p
    print(ans)


if __name__ == "__main__":
    main()
