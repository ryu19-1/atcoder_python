#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N, A, B = map(int, input().split())
    # if N == 2:
    #     print('Draw')
    if (B-A-1) % 2 == 1:
        print('Alice')
    else:
        print('Borys') 

if __name__ == "__main__":
    main()
