#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7

def main():
    N = int(input())
    ans = [0]*10**4
    for x in range(1,10**2+1):
        for y in range(1,10**2+1):
            for z in range(1,10**2+1):
                tmp = (x+y+z)**2-x*y-y*z-z*x
                if tmp <= 10**4:
                    ans[tmp-1] += 1
    for i in range(N):
        print(ans[i])

if __name__ == "__main__":
    main()
