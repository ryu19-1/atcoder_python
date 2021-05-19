#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate
import math

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if K == 0:
        print(max(A))
        exit()
    
    # 二分探索で答えxを求める
    MIN = 0
    MAX = max(A)

    while MAX - MIN > 1:
        MID = (MIN + MAX)//2
        cnt = 0
        for i in range(N):
            cnt += (A[i]-1)//MID
        if cnt <= K:
            MAX = MID
        else:
            MIN = MID
    print(MAX)

if __name__ == "__main__":
    main()
