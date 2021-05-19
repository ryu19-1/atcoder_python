#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N, *a = map(int, open(0))
    for i in range(N):
        if a[i] % 2 == 1:
            print('first')
            exit()
    print('second')

if __name__ == "__main__":
    main()
