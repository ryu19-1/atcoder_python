#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = -1
    aabs = 10**12
    amax = a[N-1]
    # print(a,amax)
    for i in range(N-1):
        tmp = abs(amax/2 - a[i])
        if tmp < aabs:
            aabs = tmp
            ans = i
    print(a[N-1], a[ans])

if __name__ == "__main__":
    main()
