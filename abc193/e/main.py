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
    T = int(input())
    for _ in range(T):
        X, Y, P, Q = map(int, input().split())
        if 2 * (X + Y) == P + Q:
            if X+Y < P:
                print('infinity')
            else:
                print(P)
        else:
            # 周期がずれる場合
            if X + Y <= P:
                diff = 2 * (X + Y) - (P + Q)
                if diff > 0:
                    cnt = (P - (X + Y) + 1 + diff - 1) // diff
                    print(cnt * (P + Q) + P, cnt, diff)
                else:
                    diff = abs(diff)
                    cnt = (2 * (X + Y) + X - (P + Q) + 1 + diff - 1) // diff
                    print(cnt * (2*(X+Y)) + X)
            elif X <= P:
                pass
            else:
                pass


if __name__ == "__main__":
    main()
