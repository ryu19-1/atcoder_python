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
    c = input()
    ans = c.count('W')
    if ans == 0 or ans == N:
        print(0)
        exit()
    
    Ws = []
    Rs = []
    for i in range(N):
        if c[i] == 'W':
            Ws.append(i)
        if c[N-1-i] == 'R':
            Rs.append(N-1-i)

    Ws.append(N+1)
    Rs.append(-1)
    tmp = 0
    while Ws[tmp] < Rs[tmp]:
        tmp += 1
    
    print(min(ans,tmp))

if __name__ == "__main__":
    main()
