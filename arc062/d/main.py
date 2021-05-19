#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    s = input()
    N = len(s)
    gnum = 0
    pnum = 0
    for i in range(N):
        if s[i] == 'g':
            gnum += 1
        else:
            pnum += 1
    print((gnum-pnum)//2)

if __name__ == "__main__":
    main()
