#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 998244353

def main():
    N, A, B, K = map(int, input().split())

    a = [None] * (N+1)
    inva = [None] * (N+1)
    a[0] = 1
    
    for i in range(1, N+1):
        a[i] = i * a[i-1] % m
    
    inva[N] = pow(a[N],m-2,m)
    for i in range(N):
        inva[N-i-1] = inva[N-i] * (N-i) % m

    ans = 0
    for i in range(N+1):
        if (K-A*i) % B == 0:
            j = (K-A*i)//B
            if 0 <= j <= N:
                tmp1 = (a[N] * inva[i] % m) * inva[N-i] % m
                tmp2 = (a[N] * inva[j] % m) * inva[N-j] % m
                ans += tmp1 * tmp2 % m
                ans %= m
    print(ans)

if __name__ == "__main__":
    main()
