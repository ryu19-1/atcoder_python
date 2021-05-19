#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = A[0]
    if N % 2 == 0:
        ans += 2 * sum(A[1:(N-2)//2+1])
    else:
        ans += 2 * sum(A[1:(N-2)//2+1]) + A[(N-2)//2+1]
    print(ans)

if __name__ == "__main__":
    main()
