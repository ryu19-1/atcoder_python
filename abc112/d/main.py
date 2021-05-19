#!/usr/bin/env python3
from bisect import bisect_left
from heapq import heappush

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

def main():
    N, M = map(int, input().split())
    ans = cal_divisors(M)
    # print(ans)
    i = bisect_left(ans,N)
    print(M//ans[i])

if __name__ == "__main__":
    main()