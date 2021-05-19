#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    a = list(map(int, input().split()))
    L = [0]*(N+1)
    R = [0]*(N+1)
    for i in range(N):
        L[i+1] = L[i]^a[i]
        R[N-i-1] = R[N-i]^a[N-i-1]
    ans = [None]*N
    for i in range(N):
        ans[i] = L[i]^R[i+1]
    print(*ans)
    # print(L,R)


if __name__ == "__main__":
    main()
