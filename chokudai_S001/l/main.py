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
    a = list(map(lambda x: int(x)-1, input().split()))
    order = [None] * N
    for i in range(N):
        order[a[i]] = i
    # print(order)
    cnt = 0
    for i in range(N):
        if order[i] == i:
            continue
        b = order[i]
        c = a[i]
        order[c] = b
        order[i] = i
        a[i] = i
        a[b] = c
        cnt += 1
    # print(cnt)
    if (N - cnt) % 2 == 0:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()
