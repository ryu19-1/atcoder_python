#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7

N, M, R = map(int, input().split())
r = list(map(int, input().split()))
    
adj = [[INF]*N for _ in range(N)]
perm_list = []

def make_permutation(l,R):
    if R == 0:
        perm_list.append(l)
    else:
        for a in r:
            if a not in l:
                make_permutation(l+[a],R-1)

def main():
    for _ in range(M):
        A, B, C = map(int, input().split())
        adj[A-1][B-1] = C
        adj[B-1][A-1] = C
    
    # 方針: Warshall-Floydで各頂点間の最短距離を求めてからrの順列全探索
    for k in range(N):# kから回さないとバグる
        for i in range(N):
            for j in range(N):
                adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][j])

    make_permutation([],R)
    ans = INF
    for ps in perm_list:
        tmp = 0
        for i in range(R-1):
            tmp += adj[ps[i]-1][ps[i+1]-1]
        ans = min(ans,tmp)
    print(ans)
    # print(perm_list)

if __name__ == "__main__":
    main()
