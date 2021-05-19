#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    print(sum(p[:K]))

if __name__ == "__main__":
    main()
