#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def cal_divisors(N):
    divisors = []
    i = 1
    while i*i < N:
        if N % i == 0:
            divisors.append(i)
        i += 1
    divisors.sort()
    return divisors

def main():
    N = int(input())
    l = cal_divisors(N)
    ans = 0
    for i in l:
        if N//i - i > 1:
            ans += N//i - 1
    print(ans)

if __name__ == "__main__":
    main()
