#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    C = [None] * N
    ans = 0
    for i in range(N):
        a, b = map(int, input().split())
        C[i] = a+b
        ans -= b
    C.sort(reverse=True)
    print(ans + sum(C[::2]))

if __name__ == "__main__":
    main()
