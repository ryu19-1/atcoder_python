#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    for h in range(1,3501):
        for n in range(1,3501):
            a = N*h*n
            b = 4*h*n - N*h - N*n
            if b != 0 and a % b == 0 and 0 < a//b <= 3500:
                print(h,n,a//b)
                exit()

if __name__ == "__main__":
    main()
