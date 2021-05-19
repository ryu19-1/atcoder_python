#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    X, Y = map(int, input().split())
    for i in range(X+1):
        for j in range(X+1):
            if i + j == X and 2*i + 4*j == Y:
                print('Yes')
                exit()
    print('No')


if __name__ == "__main__":
    main()
