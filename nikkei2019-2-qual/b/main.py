#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    D = list(map(int, input().split()))
    p = 998244353
    if D[0] > 0:
        exit(print(0))
    l = Counter(D)
    if l[0] > 1:
        exit(print(0))
    ans = 1
    for i in range(1,max(l)+1):
        if l[i] == 0:
            exit(print(0))
        ans *= pow(l[i-1],l[i],p)
        ans %= p
    print(ans)

if __name__ == "__main__":
    main()
