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
    cnt = [0] * 1000_001
    ALL = 0
    for _ in range(N):
        s = int(input())
        cnt[s] += 1
        if s > 0:
            ALL += 1
    # print(cnt[:100])
    for i in range(1000_000, 1, -1):
        cnt[i - 1] += cnt[i]
    cnt[0] = cnt[1]

    # print(cnt[:100])
    Q = int(input())
    for _ in range(Q):
        k = int(input())
        if k >= ALL:
            print(0)
            continue
        l = -1  # ちゃんと範囲外
        r = 1000_001  # ちゃんと範囲外
        while abs(r - l) > 1:  # 逆転もありうるので注意（ペナを出さないように）
            mid = (r + l) // 2
            if cnt[mid] <= k:
                r = mid
            else:
                l = mid
        print(r)


if __name__ == "__main__":
    main()
