#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush,heapify
from bisect import bisect_left

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    q = []
    for i in range(M):
        B, C = map(int, input().split())
        heappush(q,(-C,B))
    
    ans = 0
    index = 0
    # print(A)
    while q:
        c,b = heappop(q)
        c *= -1
        # print(c,b)
        count = 0
        for i in range(b):
            if i + index == N:
                break
            if c > A[index+i]:
                ans += c
                count += 1
            else:
                break

        # print(ans,index)
        if count < b:
            index += count
            break
        else:
            index += count
            
    print(ans + sum(A[index:]))

if __name__ == "__main__":
    main()
