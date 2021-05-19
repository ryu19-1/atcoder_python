#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from math import gcd

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    
    if K > A[N-1]:
        print('IMPOSSIBLE')
    else:
        ans = 0
        for i in range(N):
            ans = gcd(ans,A[i])
            if ans == 1:
                print('POSSIBLE')
                exit()
        if (A[N-1]-K)%ans == 0:#A[N-1]%ans == 0だからこれでいい
            print('POSSIBLE')
        else:
            print('IMPOSSIBLE')


if __name__ == "__main__":
    main()
