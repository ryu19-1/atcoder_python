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
    N, C = map(int, input().split())
    x = [None] * N
    v = [None] * N
    for i in range(N):
        x[i], v[i] = map(int, input().split())

    # 時計回り方向の累積和
    accumR = [0] * (2 * N + 1)
    now = 0
    for i in range(2 * N):
        accumR[i + 1] = accumR[i] + v[i % N] - (x[i % N] - now) % C
        now = x[i % N]

    # print(accumR)
    acmaxR = accumR[:]
    for i in range(2 * N):
        if acmaxR[i + 1] < acmaxR[i]:
            acmaxR[i + 1] = acmaxR[i]
    # print(acmaxR)

    # 反時計回りの累積和
    accumL = [0] * (2 * N + 1)
    now = C
    for i in range(2 * N):
        accumL[i + 1] = accumL[i] + \
            v[(N - 1 - i) % N] - (now - x[(N - 1 - i) % N]) % C
        now = x[(N - 1 - i) % N]

    # print(accumL)
    acmaxL = accumL[:]
    for i in range(2 * N):
        if acmaxL[i + 1] < acmaxL[i]:
            acmaxL[i + 1] = acmaxL[i]

    ans = 0  # 何も食べない場合もある
    # 時計回りに食べていく場合
    ans = max(ans, max(accumR[:N+1]))

    # 反時計回りに食べていく場合
    ans = max(ans, max(accumL[:N+1]))

    # 半時計->時計
    for i in range(N):  # 反時計回りにどこまで食べるか
        res = accumL[i + 1]
        res -= C - x[N - 1 - i]  # 原点に戻るまで
        res += acmaxR[N-i-1]
        ans = max(ans, res)
        # print(i, res)

    # 時計->半時計
    for i in range(N):  # 時計回りにどこまで食べるか
        res = accumR[i + 1]
        res -= x[i]  # 原点に戻るまで
        res += acmaxL[N-i-1]
        ans = max(ans, res)
    print(ans)


if __name__ == "__main__":
    main()
