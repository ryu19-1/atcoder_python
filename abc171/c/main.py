#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    a = 'zabcdefghijklmnopqrstuvwxy'
    ans = ''
    i = 0
    while N > 0:
        ans += a[N%26]
        N =  (N-1)//26
        # print(N)
    print(ans[::-1])

if __name__ == "__main__":
    main()
