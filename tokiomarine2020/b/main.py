#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    A, V = map(int, input().split())
    B, W = map(int, input().split())
    T = int(input())
    if V > W and abs(B-A)/(V-W) <= T:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()
