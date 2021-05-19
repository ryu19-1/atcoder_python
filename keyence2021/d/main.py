#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate
from math import factorial

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    N = 8
    print(factorial(pow(2, N)-1) //
          ((factorial(pow(2, N-1)-1)*factorial(pow(2, N-1))))//2)


if __name__ == "__main__":
    main()
