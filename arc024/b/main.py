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
    colors = [int(input()) for _ in range(N)]
    check = []
    now = 0
    while now < N:
        cnt = 1
        while now+cnt < N and colors[now] == colors[now + cnt]:
            cnt += 1
        check.append(cnt)
        now += cnt
    # print(check)
    if len(check) == 1:
        print(-1)
        exit()
    if colors[0] == colors[-1]:
        check[0] += check[-1]
        check = check[:-1]
    # print(check)
    print((max(check)+1)//2)


if __name__ == "__main__":
    main()
