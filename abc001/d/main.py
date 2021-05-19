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
    imos = [0] * (12 * 24 + 1)
    for _ in range(N):
        s, e = input().split('-')
        # print(s, e)
        imos[int(s)//100*12 + int(s) % 100//5] += 1
        imos[int(e)//100*12 + (int(e) % 100 + 4) // 5] -= 1
    imos = [*accumulate(imos)]
    # print(imos)
    i = 0
    while i < 12 * 24 + 1:
        ans = []
        if imos[i] > 0:
            ans.append(i // 12*100 + i % 12 * 5)
            while i < 12 * 24 + 1 and imos[i + 1] > 0:
                i += 1
            i += 1
            ans.append(i // 12*100 + i % 12 * 5)
            print('{:04}-{:04}'.format(ans[0], ans[1]))
        else:
            i += 1


if __name__ == "__main__":
    main()
