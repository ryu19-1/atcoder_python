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
    a, b, c = map(int, input().split())
    ans = [2] * (a+b+c)
    N = int(input())
    q = []

    for i in range(N):
        t = list(map(int, input().split()))
        if t[3] == 1:
            for j in range(3):
                ans[t[j] - 1] = 1
        else:
            q.append(t)

    M = len(q)
    for i in range(M):
        for j in range(M):
            cnt = 0
            alt = -1
            for k in range(3):
                if ans[q[j][k] - 1] == 1:
                    cnt += 1
                else:
                    alt = q[j][k]-1
            if cnt == 2:
                ans[alt] = 0
    [print(a) for a in ans]


if __name__ == "__main__":
    main()
