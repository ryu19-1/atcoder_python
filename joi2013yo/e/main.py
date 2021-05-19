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
    X1 = [None] * N
    X2 = [None] * N
    Y1 = [None] * N
    Y2 = [None] * N
    Z1 = [None] * N
    Z2 = [None] * N
    for i in range(N):
        X1[i], Y1[i], Z1[i], X2[i], Y2[i], Z2[i] = map(int, input().split())
    X = sorted(X1 + X2)
    Y = sorted(Y1 + Y2)
    Z = sorted(Z1 + Z2)
    # print(X, Y, Z)
    ans = 0
    for i in range(2 * N - 1):
        for j in range(2 * N - 1):
            for k in range(2 * N - 1):
                cnt = 0
                for l in range(N):
                    if X1[l] <= X[i] and X[i + 1] <= X2[l] and Y1[l] <= Y[j] \
                            and Y[j + 1] <= Y2[l] and Z1[l] <= Z[k] and Z[k + 1] <= Z2[l]:
                        cnt += 1
                if cnt >= K:
                    ans += (X[i + 1] - X[i]) * \
                        (Y[j + 1] - Y[j]) * (Z[k + 1] - Z[k])

    print(ans)


if __name__ == "__main__":
    main()
