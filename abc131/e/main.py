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
    N, K = map(int, input().split())
    if K > (N-1)*(N-2)//2:
        print(-1)
    else:
        print((N-1) + (N-1) * (N - 2) // 2 - K)
        uv = set()
        for i in range(N - 1):
            uv.add((i + 1, N))
        cnt = (N - 1) * (N - 2) // 2 - K
        # print(cnt)
        for i in range(N):
            for j in range(i + 1, N):
                if (i+1, j+1) not in uv and cnt > 0:
                    uv.add((i + 1, j + 1))
                    cnt -= 1

        [print(s[0], s[1]) for s in uv]


if __name__ == "__main__":
    main()
