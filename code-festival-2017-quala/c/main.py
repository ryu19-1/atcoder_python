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
    H, W = map(int, input().split())
    a = ''
    for _ in range(H):
        a += input()
    
    nums1 = 0
    nums2 = 0
    if H % 2 != W % 2:
        nums2 -= 1
    for l in Counter(a).values():
        if l & 1:
            nums1 += 1
        if l % 4 > 1:
            nums2 += 1

    if nums1 > H*W % 2 or nums2 > (H%2) * ((W-1)//2) + (W%2) * ((H-1)//2):
        print('No')
    else:
        print('Yes')

if __name__ == "__main__":
    main()