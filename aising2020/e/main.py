#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7

def main():
    T = int(input())
    for _ in range(T):
        # 方針:
        N = int(input())
        K = [None] * N
        34 = [None] * N
        ans = 0

        for i in range(N):
            k,l,r = map(int, input().split())
            K[i] = k
            LR[i] = (k,r-l)
            ans += r
        K.sort()
        LR.sort()
        print(LR)
        print(ans)
        
        q = []
        for i in range(N):
            for j in range(bisect_left(K,i+1),bisect_right(K,i+1)):
                heappush(q,LR[j][1])
            ans -= heappop(q)
            print(ans)
        
        # 敗因:最初から全てのラクダを入れちゃうと失敗する1日ごとにその日までのラクダをいれる
        


if __name__ == "__main__":
    main()
