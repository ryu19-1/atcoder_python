#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def prime_factorize(N):
    ans = 0
    f = 1
    while f <= N:
        ans += f * (N//f) * (N//f+1) //2
        f += 1
    return ans

def main():
    N = int(input())
    ans = prime_factorize(N)
    print(ans)

if __name__ == "__main__":
    main()
