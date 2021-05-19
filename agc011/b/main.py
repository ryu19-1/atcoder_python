#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_left

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    # print(A)
    ans = -1
    for i in range(N-1):
        if A[i]*2 < A[i+1]:
            ans = i
        A[i+1] += A[i]
    print(N-ans-1)

if __name__ == "__main__":
    main()
