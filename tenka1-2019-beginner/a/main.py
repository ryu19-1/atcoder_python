#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    A, B, C = map(int, input().split())
    if A < C < B or B < C < A:
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()
