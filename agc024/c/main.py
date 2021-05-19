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
    A = [int(input()) for _ in range(N)]
    for i in range(N):
        if A[i] > i:
            print(-1)
            exit()
    ans = 0
    now = N - 1
    while now >= 0:
        ans += A[now]
        cnt = 0
        while A[now - cnt] == A[now] - cnt:
            cnt += 1
        if A[now - cnt] < A[now] - cnt:
            print(-1)
            exit()
        now -= cnt
    print(ans)


if __name__ == "__main__":
    main()
