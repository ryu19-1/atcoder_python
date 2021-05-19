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
    K = int(input())
    tmp = 7
    i = 0
    while i < 10**6:
        # print(7*tmp)
        if tmp % K == 0:
            print(i+1)
            exit()
        else:
            tmp += 7 * pow(10,(i+1),K) % K
            tmp %= K
            i += 1 
    print(-1)

if __name__ == "__main__":
    main()
