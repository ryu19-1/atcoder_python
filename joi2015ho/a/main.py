#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

def main():
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    ans = [0]*(N)
    for i in range(M-1):
        p,q = P[i],P[i+1]
        if p > q:
            p,q = q,p
        ans[p-1] += 1
        ans[q-1] -= 1
    ans = list(accumulate(ans))

    suma = 0
    for i in range(N-1):
        a, b, c = map(int, input().split())
        suma += min(ans[i]*a,ans[i]*b+c)
    print(suma)
    

if __name__ == "__main__":
    main()
