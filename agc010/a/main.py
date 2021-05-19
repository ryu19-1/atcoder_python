#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if A[i] % 2 == 1:
            count +=1 
    if count % 2 == 0:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()
