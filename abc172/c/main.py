#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right,bisect_left
from itertools import accumulate

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = [0] + list(accumulate(A))
    B = list(accumulate(B))
    # print(A,B)
    ans = 0
    for i in range(N+1):
        if K - A[i] >= 0:
            j = bisect_right(B,K-A[i])
            # print(i,j,K-A[i])
            ans = max(ans,i+j)

    print(ans)
        


if __name__ == "__main__":
    main()
