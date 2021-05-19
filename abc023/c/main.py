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
    R, C, K = map(int, input().split())
    candyR = [0]*R
    candyC = [0]*C
    N = int(input())
    r = [None] * N
    c = [None] * N
    for i in range(N):
        r[i], c[i] = map(lambda x: int(x)-1, input().split())
        candyR[r[i]] += 1
        candyC[c[i]] += 1
    
    ans = 0
    lR = Counter(candyR)
    lC = Counter(candyC)
    # print(lR,lC)
    # 自分のところにアメがある場合は1引かないとだめ
    for x in range(K+1):
        ans += lR[x] * lC[K-x]
    
    for i in range(N):
        tmp = candyR[r[i]] + candyC[c[i]]
        if tmp == K+1:
            ans += 1
        elif tmp == K:
            ans -= 1
    print(ans)

if __name__ == "__main__":
    main()
