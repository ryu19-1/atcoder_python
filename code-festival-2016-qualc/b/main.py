#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    K, T = map(int, input().split())
    a = list(map(int, input().split()))
    print(max(0,2*max(a) - K - 1))  

if __name__ == "__main__":
    main()
