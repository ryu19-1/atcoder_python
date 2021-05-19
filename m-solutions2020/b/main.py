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
    A, B, C = map(int, input().split())
    K = int(input())
    ans = 0
    while A >= B:
        ans += 1
        B *= 2
    
    while B >= C:
        ans += 1
        C *= 2
    if ans <= K:
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()
