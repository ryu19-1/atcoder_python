#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    for i in range(N-1,-1,-1):
        if sum(b[i::i+1]) % 2 != a[i]:
            b[i] += 1
    print(b.count(1))
    for i in range(len(b)):
        if b[i] == 1:
            print(i+1)

if __name__ == "__main__":
    main()
