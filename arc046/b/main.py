#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    N = int(input())
    A, B = map(int, input().split())
    if N <= A:
        print('Takahashi')
    else:
        if A == B:
            if N % (A + 1) == 0:
                print('Aoki')
            else:
                print('Takahashi')
        else:
            if A > B:
                print('Takahashi')
            else:
                print('Aoki')


if __name__ == "__main__":
    main()
