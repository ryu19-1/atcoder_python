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
    S = input()
    N = len(S)
    T = input()
    M = len(T)
    ans = INF
    for i in range(N-M+1):
        cnt = 0
        for k in range(M):
            if S[i+k] != T[k]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

if __name__ == "__main__":
    main()