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
    a = list(map(int, input().split()))
    ans = []
    while True:
        if min(a) >= 0:
            for i in range(N - 1):
                ans.append((i+1, i+2))
                # print(i+1, i + 2)
            break
        elif max(a) <= 0:
            for i in range(N - 1, 0, -1):
                ans.append((i+1, i))
                # print(i+1, i)
            break
        else:
            absmax = 0
            j = -1
            for i in range(N):
                if abs(a[i]) > absmax:
                    absmax = abs(a[i])
                    j = i
            add = a[j]
            for i in range(N):
                ans.append((j+1, i+1))
                # print(j+1, i+1)
                a[i] += add
            # print(a)
    print(len(ans))
    [print(*a) for a in ans]


if __name__ == "__main__":
    main()
