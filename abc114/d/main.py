#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7

def cal_divisors(N):
    divisors = []
    i = 1
    while i*i <= N:
        if N % i == 0:
            divisors.append(i)
            if i != N // i:
                divisors.append(N//i)
        i += 1
    divisors.sort()
    return divisors

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
    divisors = []
    for i in range(1,N+1):
        divisors.extend(prime_factorize(i))
    l = Counter(divisors)
    # print(l)
    # 約数を75個持つ X = a^p * b^q とした時、(p,q) = (0,74), (2,24), (4,14) しかない
    ans = 0
    nums = l.values()
    # 74より大きい素因数の数だけ(1)のパターン
    ans += len([*filter(lambda x: x >= 74, nums)])

    # 14,4のパターン
    ans += len([*filter(lambda x: x >= 14, nums)]) * (len([*filter(lambda x: x >= 4, nums)])-1)

    # 24,2のパターン
    ans += len([*filter(lambda x: x >= 24, nums)]) * (len([*filter(lambda x: x >= 2, nums)])-1)

    # 4,4,2のパターン
    ans += len([*filter(lambda x: x >= 4, nums)]) * (len([*filter(lambda x: x >= 4, nums)])-1) * (len([*filter(lambda x: x >= 2, nums)])-2) // 2

    print(ans)

if __name__ == "__main__":
    main()
