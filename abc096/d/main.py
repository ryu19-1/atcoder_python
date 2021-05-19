#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right, bisect_left
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7

# N以下の素数列挙(エラトステネスの篩)
def cal_primes(N):
    # 素数候補をリストでもつ
    candidate = [*range(2, N+1)]
    primes = []

    while candidate[0]**2 <= N:
        primes.append(candidate[0])
        candidate = [*filter(lambda x: x % candidate[0] != 0, candidate)]
    
    primes.extend(candidate)
    return primes

def main():
    N = int(input())
    primes = cal_primes(55555)
    primes = [*filter(lambda x: x % 5 == 1, primes)]

    print(*primes[:N])


if __name__ == "__main__":
    main()
