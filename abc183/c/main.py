#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate, permutations

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for p in permutations(range(1, N)):
        # print(p)
        res = T[0][p[0]]
        for i in range(N - 2):
            res += T[p[i]][p[i + 1]]
        res += T[p[N - 2]][0]
        if res == K:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
