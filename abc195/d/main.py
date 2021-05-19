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
    N, M, Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    WV.sort(key=lambda x: x[1], reverse=True)
    # print(WV)

    X = list(map(int, input().split()))

    for _ in range(Q):
        L, R = map(int, input().split())
        # 使える箱
        L -= 1
        R -= 1
        y = X[:L] + X[R + 1:]
        y.sort()
        # print(y)
        used = [False] * len(y)
        ans = 0
        # 小さい箱からみて、自分が入れられる
        for i in range(N):
            # print(WV[i])
            for j in range(len(y)):
                if used[j] is False and WV[i][0] <= y[j]:
                    used[j] = True
                    ans += WV[i][1]
                    break
        print(ans)


if __name__ == "__main__":
    main()
