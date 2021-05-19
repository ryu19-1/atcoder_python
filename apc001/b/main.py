#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    pos = 0
    neg = 0
    for i in range(N):
        pos += max(a[i]-b[i],0)
        neg += abs(min(a[i]-b[i],0))//2
    if  neg >= pos:
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()
