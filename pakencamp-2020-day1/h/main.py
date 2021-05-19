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
    T = int(input())
    for _ in range(T):
        A, B, C = map(int, input().split())
        print(B ^ C == A, A ^ C == B)
        if B ^ C == A:
            print('Yes')
        else:
            print('No')


if __name__ == "__main__":
    main()
