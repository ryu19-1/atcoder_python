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
    A = input()
    N = len(A)
    ans = N * 25
    cnt = 0
    for i in range(N // 2):
        if A[i] != A[N - 1 - i]:
            cnt += 1
    if N % 2 == 1:
        if cnt == 0:
            print(ans - 25)
        elif cnt == 1:
            print(ans - 2)
        else:
            print(ans)
    else:
        if cnt == 1:
            print(ans - 2)
        else:
            print(ans)


if __name__ == "__main__":
    main()
