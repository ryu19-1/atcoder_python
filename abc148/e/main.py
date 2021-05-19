#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
import math

def main():
    N = int(input())
    if N % 2 == 1:
        print(0)
    else:
        ans = 0
        tmp = 10
        while tmp <= N:
            ans += N//tmp
            tmp *= 5
        print(ans)

if __name__ == "__main__":
    main()
