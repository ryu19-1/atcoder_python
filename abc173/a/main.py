#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    if N % 1000 == 0:
        print(0)
    else:
        print(1000 - N%1000)

if __name__ == "__main__":
    main()
