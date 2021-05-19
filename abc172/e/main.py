#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N, M = map(int, input().split())
    p = 10**9 + 7
    
    a = [None] * (M+1)
    inva = [None] * (M+1)
    a[0] = 1
    for i in range(1, M+1):
        a[i] = i * a[i-1] % p
    inva[M] = pow(a[M],p-2,p)
    for i in range(M):
        inva[M-i-1] = inva[M-i] * (M-i) % p

    ans = 0
    for k in range(N+1):
        # nCk
        tmp = (a[N] * inva[N-k] % p) * inva[k] % p
        # (-1)**k
        if k % 2 == 1:
            tmp = -tmp % p
        # mPk
        tmp = (tmp * a[M] % p) * inva[M-k] % p

        # m-kPn-k
        tmp *= pow(a[M-k] * inva[M-N] % p, 2, p)
        tmp %= p
        ans += tmp
        ans %= p
    print(ans)

if __name__ == "__main__":
    main()
