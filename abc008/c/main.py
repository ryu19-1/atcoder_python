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
    C = [int(input()) for _ in range(N)]
    C.sort()
    adj = [[] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j: continue
            if C[j] % C[i] == 0:
                adj[j].append(i)

    ans = 0
    for i in range(N):
        # print(i,C[i],[C[j] for j in adj[i]])
        L = len(adj[i])
        k = L//2
        # print(i,L,k)
        ans += (k+1) / (L+1)
    print(ans) 

if __name__ == "__main__":
    main()
