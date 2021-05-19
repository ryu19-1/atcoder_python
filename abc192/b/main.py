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
    S = input()
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i].islower():
                pass
            else:
                print('No')
                exit()
        else:
            if S[i].isupper():
                pass
            else:
                print('No')
                exit()
    print('Yes')


if __name__ == "__main__":
    main()
