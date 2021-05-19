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
    AB = [list(map(int, input().split())) for _ in range(N)]
    ans = INF
    for i in range(N):
        for j in range(N):
            if i != j:
                res = max(AB[i][0], AB[j][1])
            else:
                res = AB[i][0] + AB[j][1]
            ans = min(ans, res)
    print(ans)


if __name__ == "__main__":
    main()
