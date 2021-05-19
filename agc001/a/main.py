#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(1,2*N):
        ans += L[i-1]
        L[i] -= L[i-1]
    print(ans)

if __name__ == "__main__":
    main()
