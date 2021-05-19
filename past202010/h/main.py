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
    N, M, K = map(int, input().split())
    S = [list(input()) for _ in range(N)]
    # countを二次元累積和でもっておく
    count = [[[0] * (M+1) for _ in range(N+1)] for _ in range(10)]
    for i in range(N):
        for j in range(M):
            count[int(S[i][j])][i+1][j+1] += 1

    for k in range(10):
        for i in range(N):
            for j in range(M):
                count[k][i + 1][j + 1] += count[k][i + 1][j]
            for j in range(M+1):
                count[k][i + 1][j] += count[k][i][j]

    # print(count[1])

    for n in range(min(N, M), 0, -1):
        # print(n)
        for i in range(N - n + 1):
            for j in range(M - n + 1):
                # (i,j)~(i+n,j+n)の中にある数字の数+Kがn**2を超えていたらok
                for k in range(10):
                    # print(n, i, j, k)
                    cnt = count[k][i + n][j + n] - count[k][i +
                                                            n][j] - count[k][i][j + n] + count[k][i][j]
                    if cnt + K >= n * n:
                        print(n)
                        exit()


if __name__ == "__main__":
    main()
