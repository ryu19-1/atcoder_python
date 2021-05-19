#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_left
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    N = int(input())
    S = input()
    T = input()
    idx = []
    for i in range(N):
        if S[i] == '1':
            idx.append(i)
    # print(idx)
    ans = 0
    for i in range(N - 1, -1, -1):
        if T[i] == '1':
            if len(idx) == 0:
                print(-1)
                exit()
            d = bisect_left(idx, i)
            if d >= len(idx):
                print(-1)
                exit()
            ans += idx[d] - i
            del idx[d]
    # print(ans, idx)
    if len(idx) % 2 == 1:
        print(-1)
        exit()
    # for j in range(len(idx) // 2):
    ans += sum(idx[1::2]) - sum(idx[::2])
    print(ans)


if __name__ == "__main__":
    main()
