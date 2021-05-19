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
    S = input().lower()
    # print(S)
    N = len(S)
    for i in range(N):
        if S[i] != 'i':
            continue
        for j in range(i + 1, N):
            if S[j] != 'c':
                continue
            for k in range(j + 1, N):
                if S[k] == 't':
                    print('YES')
                    exit()
    print('NO')


if __name__ == "__main__":
    main()
