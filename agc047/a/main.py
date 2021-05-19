#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate
import copy

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7

def main():
    N = int(input())
    M = 101
    offset = M//2
    cnt = [[0]*M for _ in range(M)]
    p = [None for _ in range(N)]
    for i in range(N):
        A = input()
        n = len(A)
        tmp = [0,0]# 2と5の数を調べる。-は不足
        if '.' in A:
            tmp[0] -= n-1-A.index('.')
            tmp[1] -= n-1-A.index('.')
        A = int(A.replace('.',''))
        while A % 2 == 0:
            A //= 2
            tmp[0] += 1
        while A%5 == 0:
            A //= 5
            tmp[1] += 1
        cnt[offset+tmp[0]][offset+tmp[1]] += 1
        p[i] = (tmp[0]+offset, tmp[1]+offset)
    # print(cnt)
    cnt2 = copy.deepcopy(cnt)

    # 累積和をとる
    for i in range(M-1,-1,-1):
        for j in range(M-1,-1,-1):
            if j < M-1:
                cnt[i][j] += cnt[i][j+1]
    
    for i in range(M-1,-1,-1):
        for j in range(M-1,-1,-1):
            if i < M-1:
                cnt[i][j] += cnt[i+1][j]
    
    # print(cnt)
    ans = 0
    for i in range(M):
        for j in range(M):
            if cnt2[i][j]==0: continue
            ans += cnt2[i][j]*cnt[offset*2-i][offset*2-j]
            # print(p[i])
            # print(cnt[offset*2-p[i][0]][offset*2-p[i][1]])
            # ans += cnt[offset*2-p[i][0]][offset*2-p[i][1]]
            # print(i,j,cnt2[i][j],ans)
    print((ans-cnt[offset][offset])//2)

if __name__ == "__main__":
    main()
