#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    H, W, A, B = map(int, input().split())
    [print('0'*A + '1'*(W-A)) for _ in range(B)]
    [print('1'*A + '0'*(W-A)) for _ in range(H-B)]

if __name__ == "__main__":
    main()
