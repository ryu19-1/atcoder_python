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
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    cost = [0]*N# cost[i]: i番目で買ってから最適に売ることで得られる利益
    q = []
    heappush(q,-A[N-1])
    for i in range(N-2,-1,-1):
        v = heappop(q)
        cost[i] = -v-A[i]
        heappush(q,v)
        heappush(q,-A[i])
    # print(cost)
    print(cost.count(max(cost)))

if __name__ == "__main__":
    main()
