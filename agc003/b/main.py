#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N, *A = map(int, open(0))
    ans = 0
    i = 0
    prev = 0
    while i < N:
        if A[i] == 0:
            prev = 0
        else:
            ans += (A[i]+prev)//2
            prev = (A[i]+prev)%2
        # print(A[i],prev,ans)
        i += 1
    print(ans)

if __name__ == "__main__":
    main()
