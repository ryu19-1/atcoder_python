#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    a = int(input())
    print(a+a**2+a**3)

if __name__ == "__main__":
    main()
