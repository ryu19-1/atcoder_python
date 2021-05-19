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
    N, K = map(int, input().split())
    # (1) K,K,Kの1通り
    # (2) 1~(K-1),K,Kの2*(K-1)通り
    # (3) K,K,(K+1)~Nの2*(N-K)通り
    # (4) 1~(K-1),K,(K+1)~Nの6*(N-K)*(K-1)通り
    count = 1 + 3*(K-1) + 3*(N-K) + 6*(K-1)*(N-K)
    print(count/pow(N,3))

if __name__ == "__main__":
    main()
