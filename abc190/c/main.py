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
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(1 << K):
        ball = set()
        for j in range(K):
            if (i >> j) & 1:
                ball.add(CD[j][0])
            else:
                ball.add(CD[j][1])
        # print(i, ball)
        res = 0
        for j in range(M):
            if AB[j][0] in ball and AB[j][1] in ball:
                res += 1
        ans = max(ans, res)
        # print(i, ball, res)
    print(ans)


if __name__ == "__main__":
    main()
