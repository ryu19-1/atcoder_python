#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = set()
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] //= 2
        b.add(a[i])
    print(len(b))

if __name__ == "__main__":
    main()
