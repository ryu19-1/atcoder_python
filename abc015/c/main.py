#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

N, K = map(int, input().split())
T = []
for i in range(N):
    T.append(list(map(int, input().split())))

def saiki(xor,i):
    if i == N:
        if xor == 0:
            print('Found')
            exit()
    else:
        for j in range(K):
            saiki(xor^T[i][j],i+1)

xor = 0
saiki(xor,0)
print('Nothing')
