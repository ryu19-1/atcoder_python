#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N, K = map(int, input().split())
    p = 10**9+7

    # 階乗の事前計算
    a = [None] * (N+1)
    inva = [None] * (N+1)
    a[0] = 1
    
    for i in range(1, N+1):
        a[i] = i * a[i-1] % p
    
    inva[N] = pow(a[N],p-2,p)
    for i in range(N):
        inva[N-i-1] = inva[N-i] * (N-i) % p

    for i in range(1,K+1):
        if N-K < i-1:
            print(0)
            continue
        tmp = ((a[K-1] * inva[K-i]) % p) * inva[i-1] % p
        tmp2 = ((a[N-K+1] * inva[N-K-i+1]) % p) * inva[i] % p
        print(tmp * tmp2 % p)


if __name__ == "__main__":
    main()
