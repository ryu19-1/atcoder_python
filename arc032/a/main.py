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
    if N == 1:
        print('BOWWOW')
        exit()
    N = N * (N + 1) // 2
    if len(prime_factorize(N)) == 1:
        print('WANWAN')
    else:
        print('BOWWOW')


if __name__ == "__main__":
    main()
