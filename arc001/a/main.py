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
    cnt = [0] * 4
    S = input()
    for i in range(N):
        cnt[int(S[i]) - 1] += 1
    print(max(cnt), min(cnt))


if __name__ == "__main__":
    main()
