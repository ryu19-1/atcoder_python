#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    a = input()
    if a == a.upper():
        print('A')
    else:
        print('a')

if __name__ == "__main__":
    main()
